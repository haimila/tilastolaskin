import statistics

print("Tervetuloa laskinsovellukseen!")
print("Voit laskea lukusarjan keskiarvon, mediaanin, tai moodin.\n")

while True:

    lukulista_str = input("Syötä haluamasi luvut pilkulla erotettuna:")

    lukulista_ennen_int = (lukulista_str.split(","))
    lukulista = []

    try:

        for luku in lukulista_ennen_int:
            lukulista.append(float(luku))

    except:
        print("Lukusarjasi sisältää kirjaimia, käytä pelkkiä numeroita!")
        continue

    print("Valitse 1, 2, tai 3:\n")
    print("1. Laske keskiarvo")
    print("2. Laske mediaani")
    print("3. Laske moodi\n")
    prosessi = input("Minkä toimenpiteen haluat tehdä syöttämällesi lukusarjalle?")

    try:

        if prosessi == "1":
            print(f"Lukusarjasi keskiarvo on {statistics.mean(lukulista)}.")

        elif prosessi == "2":
            print(f"Lukusarjasi mediaani on {statistics.median(lukulista)}.")

        elif prosessi == "3":
            print(f"Lukusarjasi moodi on {statistics.mode(lukulista)}.")

        else:
            print(f"Valitse 1, 2, tai 3!")
            continue

    except:
        print("Laskennassa tapahtui virhe, syötä uudet luvut.")
        continue

    uudestaan = input("Haluatko syöttää uuden lukusarjan? K/E")

    if uudestaan == "K".lower():
        continue

    else:
        break

