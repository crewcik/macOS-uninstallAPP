import os

def uygulama_kaldir(uygulama_adi):
    uygulama_yolu = f"/Applications/{uygulama_adi}.app"
    if os.path.exists(uygulama_yolu):
        try:
            os.system(f"sudo rm -rf '{uygulama_yolu}'")
            print(f"{uygulama_adi} başarıyla uygulaması kaldırıldı.")
        except Exception as e:
            print(f"Hata: {e}")
    else:
        print(f"{uygulama_adi} Böyle bir uygulama mac'te yüklü değil.")

uygulama_adi = "Silinecek Uygulama adı: "
uygulama_kaldir(uygulama_adi)

# Selam, macOS'da program kaldırmak çok zor bu yüzden sizler için bir prgoram geliştirdik. Bu kod ile belirtilen uygulamayı macos içerisinden silmeye yarıyan sistemdir.
# Bu program Crew.dev tarafından kodlanmıştır.
