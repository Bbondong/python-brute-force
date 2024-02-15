import time


# Méthode de brute force (toutes les combinaisons)
def brute_force(mot_de_passe_cible):
    # Caractères possibles pour générer les mots de passe
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
    longueur_mot_de_passe = 1
    
    # Boucle jusqu'à ce que le mot de passe soit trouvé
    while True:
        # Génère toutes les combinaisons de mots de passe de la longueur actuelle
        for mot_de_passe in generer_mots_de_passe(caracteres, longueur_mot_de_passe):
            #print(f"Test actuel : {mot_de_passe}")
            if mot_de_passe == mot_de_passe_cible:  # Vérifie si le mot de passe actuel correspond au mot de passe cible
                return mot_de_passe                 # Renvoie le mot de passe si trouvé
        longueur_mot_de_passe += 1                  # Augmente la longueur du mot de passe si non trouvé


# Génère toutes les combinaisons possibles de mots de passe d'une longueur donnée
def generer_mots_de_passe(caracteres, longueur):
    # Cas de base: si la longueur est 0, renvoie une chaîne vide
    if longueur == 0:
        yield ''
    else:
        # Pour chaque caractère possible, génère récursivement les mots de passe de longueur - 1
        for caractere in caracteres:
            for mot_de_passe in generer_mots_de_passe(caracteres, longueur - 1):
                yield caractere + mot_de_passe  # Ajoute le caractère actuel à chaque mot de passe généré


# Méthode avec un dictionnaire
def attaque_dictionnaire(mot_de_passe_cible, dictionnaire):
    with open(dictionnaire, 'r') as fichier:  # Ouvre le fichier contenant le dictionnaire de mots
        for mot in fichier:                   # Parcours chaque mot dans le dictionnaire
            mot = mot.strip()                 # Supprime les espaces et sauts de ligne
            if mot == mot_de_passe_cible:     # Vérifie si le mot actuel correspond au mot de passe cible
                return mot                    # Renvoie le mot de passe si trouvé
    return None                               # Renvoie None si le mot de passe n'est pas trouvé dans le dictionnaire


# Test du programme
if __name__ == "__main__":
    mot_de_passe_cible = input("Entrez un mot de passe à trouver : ")
    dictionnaire_fichier = "dictionnaire.txt"


    # Brute force
    print("\n\nAttaque par brute force :\n")
    debut = time.time()
    resultat = brute_force(mot_de_passe_cible)
    fin = time.time()

    if resultat:
        print("Mot de passe trouvé :", resultat)
    else:
        print("Mot de passe non trouvé")

    print(f"Trouvé en {round(fin-debut, 2)}s.\n\n")


    # Dictionnaire
    print("Attaque par dictionnaire :\n")
    debut = time.time()
    resultat = attaque_dictionnaire(mot_de_passe_cible, dictionnaire_fichier)
    fin = time.time()

    if resultat:
        print("Mot de passe trouvé :", resultat)
    else:
        print("Mot de passe non trouvé")

    print(f"Trouvé en {round(fin-debut, 2)}s.\n\n")

input("Appuyez sur une touche pour quitter...")
