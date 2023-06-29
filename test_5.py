import random

nombre_secret = random.randint(1, 100)

compteur = 0

print("Devinez le nombre secret entre 1 et 100 :")

while True:
    proposition = int(input("Votre proposition : "))
    compteur += 1

    if proposition < nombre_secret:
        print("Le nombre secret est plus grand que", proposition)
    else:
        if proposition > nombre_secret:
            print("Le nombre secret est plus petit que", proposition)
        else:
            print("Félicitations ! Vous avez trouvé le nombre secret en", compteur, "tentatives.")
            break
