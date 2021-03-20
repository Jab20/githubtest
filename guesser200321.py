import random
print("Wilkommen zum Zahlen raten!")
versuche = 7
zufallsZahl = random.randint(1,100)
while versuche > 0:
    versuche -= 1
    print("Deine Schätzung:")
    inpt = input()
    a = int(inpt)
    if zufallsZahl>a:
        print("Die gesuchte Zahl ist grösser.")
    if zufallsZahl<a:
        print("Die gesuchte Zahl ist kleiner")
    elif zufallsZahl == a:
        print("Du hast die gesuchte Zahl gefunden!")
        print("Du hattest noch " + str(versuche) + "")
        break
    print("Du hast noch " + str(versuche) + " Versuche übrig")
    if versuche == 0:
        print("Du hast leider verloren! Spiel nocheinmal.")
