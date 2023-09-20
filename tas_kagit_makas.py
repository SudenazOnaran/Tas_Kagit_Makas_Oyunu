"""Taş kağıt makas oyunu 3 yapan kazanır"""

import random

secenekler=["tas","kagit","makas"]

bilgisayar_puanı=0
oyuncu_puani=0
print("""Tas,kagit,makas seçeneklerinden birini seç ve bilgisayarı yenmeye çalış...3 yapan kazanır""")
oyuncu_ismi=input("Oyuncunun ismini gir:")
while True:
    bilgisayar_secimi = random.choice(secenekler)
    secim = input("Seçimini gir:")
    print(f"Bilgisayarın seçimi:{bilgisayar_secimi}")
    if secim=="tas" and bilgisayar_secimi=="makas":
        print("{} kazandı... :) ".format(oyuncu_ismi))
        bilgisayar_puanı+=0
        oyuncu_puani+=1
        print("Bilgisayar puanı:",bilgisayar_puanı)
        print("{} puanı : {}".format(oyuncu_ismi,oyuncu_puani))
    elif secim=="tas" and bilgisayar_secimi=="kagit":
        print("Bilgisayar kazandı... :( ")
        bilgisayar_puanı+=1
        oyuncu_puani+=0
        print("Bilgisayar puanı:", bilgisayar_puanı)
        print("{} puanı : {}".format(oyuncu_ismi, oyuncu_puani))
    elif secim=="tas" and bilgisayar_secimi=="tas":
        print("Berabere...kimse puan almadı")
        bilgisayar_puanı+=0
        oyuncu_puani+=0
        print("Bilgisayar puanı:", bilgisayar_puanı)
        print("{} puanı : {}".format(oyuncu_ismi, oyuncu_puani))
    elif secim=="kagit" and bilgisayar_secimi=="tas":
        print("{} kazandı... :)".format(oyuncu_ismi))
        bilgisayar_puanı += 0
        oyuncu_puani += 1
        print("Bilgisayar puanı:", bilgisayar_puanı)
        print("{} puanı : {}".format(oyuncu_ismi, oyuncu_puani))
    elif secim == "kagit" and bilgisayar_secimi == "kagit":
        print("Berabere...kimse puan almadı")
        bilgisayar_puanı += 0
        oyuncu_puani += 0
        print("Bilgisayar puanı:", bilgisayar_puanı)
        print("{} puanı : {}".format(oyuncu_ismi, oyuncu_puani))
    elif secim == "kagit" and bilgisayar_secimi == "makas":
        print("Bilgisayar kazandı... :(")
        bilgisayar_puanı+=1
        oyuncu_puani+=0
        print("Bilgisayar puanı:", bilgisayar_puanı)
        print("{} puanı : {}".format(oyuncu_ismi, oyuncu_puani))
    elif secim == "makas" and bilgisayar_secimi == "tas":
        print("Bilgisayar kazandı... :(")
        bilgisayar_puanı+=1
        oyuncu_puani+=0
        print("Bilgisayar puanı:", bilgisayar_puanı)
        print("{} puanı : {}".format(oyuncu_ismi, oyuncu_puani))
    elif secim == "makas" and bilgisayar_secimi == "makas":
        print("Berabere...kimse puan almadı")
        bilgisayar_puanı += 0
        oyuncu_puani += 0
        print("Bilgisayar puanı:", bilgisayar_puanı)
        print("{} puanı : {}".format(oyuncu_ismi, oyuncu_puani))
    elif secim == "makas" and bilgisayar_secimi == "kagit":
        print("{} kazandı... :) ".format(oyuncu_ismi))
        bilgisayar_puanı+=0
        oyuncu_puani+=1
        print("Bilgisayar puanı:", bilgisayar_puanı)
        print("{} puanı : {}:".format(oyuncu_ismi, oyuncu_puani))
    if bilgisayar_puanı==3:
        print("Oyunu bilgisayar kazandı :((")
        break
    elif oyuncu_puani==3:
        print("Oyunu {} kazandı... :)) ".format(oyuncu_ismi))
        break

