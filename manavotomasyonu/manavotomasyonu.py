halsebze=["pırasa", "brokoli", "patlıcan", "kabak"]
halsebzekg=[50,60,70,80]
halmeyve=["muz", "çilek", "böğürtlen", "elma"]
halmeyvekg=[10,20,30,40]

manavsebze=[]
manavmeyve=[]
manavsebzekg=[]
manavmeyvekg=[]

sepet=[]
sepetkg=[]

while True:
    anamenu=int(input("LÜTFEN SEÇİM YAPIN\n1-hal\n2-manav\n3-fiş\n4-çıkış\n"))
    if anamenu==1:
        while True:
            halsecim=int(input("1-meyve\n2-sebze\n3-çıkış"))
            if halsecim==1:
                for i,m in enumerate(halmeyve):
                    print(f"{i}-{m}", end=" ")
                for i,kg in enumerate(halmeyvekg):
                    print(f"{i}-{kg}", end=" ")
                halmeyveal=int(input("Meyve seçimi yapın"))
                halmeyvekgal=int(input("kg seçimi yapınız"))



                if halmeyvekgal > halmeyvekg[halmeyveal]:
                    print("bu kadar kg mevcut değildir")

                else:
                    manavmeyve.append(halmeyve[halmeyveal])
                    manavmeyvekg.append(halmeyvekgal)
                    halmeyvekg[halmeyveal] -= halmeyvekgal


            if halsecim==2:


                    for i,s in enumerate(halsebze):
                        print(f"{i}-{s}", end=" ")

                    for i,kg in enumerate(halsebzekg):
                        print(f"{i}-{kg}", end=" ")

                    halsebzeal=int(input("Sebze seçimi yapın"))
                    halsebzekgal=int(input("Kg seçimi yapın"))

                    if halsebzekgal>halsebzekg[halsebzeal]:
                         print("bu kadar kg mevcut değildir")

                    else:
                         manavsebze.append(halsebze[halsebzeal])
                         manavsebzekg.append(halsebzekgal)
                         halsebzekg[halsebzeal]-= halsebzekgal

            if halsecim==3:
                break


    if anamenu==2:
        while True:
            manavsecim=int(input("1-meyve\n2-sebze\n3-çıkış"))
            if manavsecim==1:
                for i,m in enumerate(manavmeyve):
                    print(f"{i}-{m}", end=" ")
                for i,kg in enumerate(manavmeyvekg):
                    print(f"{i}-{kg}", end=" ")

                meyveal=int(input("meyve seçimi"))
                meyvekgal=int(input("kg seçimi yapın"))

                if meyvekgal>manavmeyvekg[meyveal]:
                    print("bu kadar kg mecvut değil")

                else:
                    sepet.append(manavmeyve[meyveal])
                    sepetkg.append(meyvekgal)
                    manavmeyvekg[meyveal]-=meyvekgal

            if manavsecim==2:
                for i,s in enumerate(manavsebze):
                    print(f"{i}-{s}", end=" ")
                for i,kg in enumerate(manavsebzekg):
                    print(f"{i}-{kg}", end=" ")

                sebzeal=int(input("sebze seçimi yapın"))
                sebzekgal=int(input("kg seçimi yapın"))

                if sebzekgal<manavsebzekg[sebzeal]:
                    print("bu kadar kg yok")

                else:
                    sepet.append(manavsebze[sebzeal])
                    sepetkg.append(sebzekgal)
                    manavsebzekg[sebzeal]-=sebzekgal

            if manavsecim==3:
                break

    if anamenu==3:
        if len(sepet) and len(sepetkg):
            print(list(zip(sepet, sepetkg)))
        else:
            print("Ürün seçimi yapmadınız")

    if anamenu==4:
        break













