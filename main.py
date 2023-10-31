## Crée par Dorian Figueiras le 31/10/2023


import random

difficultéDemandé = False
trouvé = False
nb_max = 0
difficulté = 0
nombreEssaie = 0 
nbPersonalisé = 0


print("Bienvenue au jeu du juste prix.")
print("")

while difficultéDemandé != True:
    
    difficulté = input("Veuillez choisir une difficulté 1 = 100 nombres, 2 = 200 nombres, 3= 300 nombres, 4 = Personalisé : ")
    
    if difficulté == str(1):
        print("Vous avez choisi la dificulté : facile.")
        difficultéDemandé = True
        nb_max = 100
        print("Vous devez trouver un nombre entre 0 et", str(nb_max))
    elif difficulté == str(2):
        print("Vous avez choisi la dificulté : moyen.")
        difficultéDemandé = True
        nb_max = 200
        print("Vous devez trouver un nombre entre 0 et", str(nb_max))
    elif difficulté == str(3):
        print("Vous avez choisi la dificulté : difficile.")
        difficultéDemandé = True
        nb_max = 300
        print("Vous devez trouver un nombre entre 0 et", str(nb_max))
    elif difficulté == str(4):
        difficultéDemandé = True
        nbPersonalisé = input("Veuillez entrer un nombre maximum pour le jeu :")
        nb_max = int(nbPersonalisé)
        print("Vous devez trouver un nombre entre 0 et", str(nb_max))
    else:
        print("Veuillez rentrer une valeur entre 1 et 3.")

nombre = random.choice(range(0, nb_max))


while trouvé != True:
    
    nombreDonné = input("Veuillez entrer un nombre :")
    
    
    
    if int(nombreDonné) < nombre:
        print("Le nombre est plus grand !")
        nombreEssaie = nombreEssaie + 1
    elif int(nombreDonné) > nombre:
        print("Le nombre est plus petit !")
        nombreEssaie = nombreEssaie + 1 
    elif int(nombreDonné) == nombre:
        nombreEssaie = nombreEssaie +1
        print("Le nombre est bien", nombre ,"FÉLICITATIONS !!")
        print("Vous avez trouvé le nombre en ", nombreEssaie ,"essais.")
        trouvé = True
    else:
        print("Le nombre entré n'est pas correct !")




