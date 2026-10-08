import os
import shutil

def build():
    # Çıktı dizinini temizle ve oluştur
    if os.path.exists('public'):
        shutil.rmtree('public')
    os.makedirs('public', exist_ok=True)
    
    # Asset'leri kopyala
    if os.path.exists('olay-ufku/assets'):
        shutil.copytree('olay-ufku/assets', 'public/assets')

    # HTML başlık ve stil kodları (sunucu.py'deki ile aynı)
    HEAD = (
        '<!doctype html><html lang="tr"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
        '<link rel="icon" type="image/png" sizes="32x32" href="assets/icon-32.png">'
        '<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">'
        '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>'
    )

    # index.html'i oku ve başlık/kapanış etiketleriyle birleştir
    with open('olay-ufku/index.html', 'r', encoding='utf-8') as f:
        body = f.read()

    with open('public/index.html', 'w', encoding='utf-8') as f:
        f.write(HEAD + body + '</body></html>')
        
    print("Build tamamlandı. public/ dizini oluşturuldu.")

if __name__ == '__main__':
    build()
