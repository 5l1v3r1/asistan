uyg_adi = "Ziks Deneme"
cizgi = "-" * 30

def metinharf():
    print(cizgi)
    dosyaadi = input(f"{cizgi}\nLütfen dosyanızın sonunda .TXT olmadan belirtiniz.\nDosyanın bu uygulama ile aynı dizinde bulunduğundan emin olunuz.\nLütfen dosyanızın adını giriniz: ")
    dosyaadi = dosyaadi + ".txt"
    try:
        with open(dosyaadi, 'r') as dosya:
            dosyaveri = dosya.read()
        print(f"{cizgi}\nMakalenizin uzunluğu (harf):", len(dosyaveri) + f"\n{cizgi}")
        baska = input("E/H\nBaşka bir dosyaya da bakmak ister misiniz?\nİşleminiz: ")
        if baska.lower() == "e":
            return dosyaadi
        else:
            return giris
    except FileNotFoundError:
        print(f"{cizgi}\nLütfen dosyanızın {__file__}'da olduğundan emin olunuz.")

def sayi_olusturucu():
    try:
        kacakadar = int(input("Kaça kadar sayı oluşturmak istiyorsunuz? "))
        atlanacak = int(input("Örn: 1-3-5-7-9-11\nSayıların arasında atlama olsun mu? Olmasını istemiyorsanız boş bırakın: "))
        if atlanacak != "":
            for sayilar in range(0, kacakadar, atlanacak):
                print(sayilar)
        else:
            for sayilar in range(0, kacakadar):
                print(sayilar)

    except TypeError:
        print("Lütfen sadece sayı giriniz.")

while True:
    giris = input(f"Merhaba değerli kullanıcı!\n{uyg_adi}'a hoş geldin.\nKullanabileceğiniz işlemler aşağıda listelenmiştir.\n\n1 - Makale Harf Sayıcı\n2 - Sayı Oluşturucu\n\n{cizgi}\nİşleminiz: ")

    if giris == "1":
        metinharf()

    elif giris == "2":
        sayi_olusturucu()

    else:
        print(f"Bir şeyler hatalı gitti.\n{cizgi}")
