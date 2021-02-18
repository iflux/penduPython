import random
import time
import sys
from datetime import datetime
dessin_pendu =[
"""------------------
    |
    |
    |
    |
    |
    |
    |
    |
   /|\               
  / | \              
 /  |  \             
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
"""
,
"""------------------
    |        |
    |        |
    |
    |
    |
    |
    |
    |
   /|\               
  / | \              
 /  |  \             
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
"""
,
"""------------------
    |        |
    |        |
    |       / \      
    |       \_/      
    |
    |
    |
    |
   /|\               
  / | \              
 /  |  \             
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
"""
,
"""------------------
    |        |
    |        |
    |       / \      
    |       \_/      
    |        |
    |        |
    |        |
    |
   /|\               
  / | \              
 /  |  \             
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
"""
,
"""------------------
    |        |
    |        |
    |       / \      
    |       \_/      
    |        |__
    |        |
    |        |
    |
   /|\               
  / | \              
 /  |  \             
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
"""
,
"""------------------
    |        |
    |        |
    |       / \      
    |       \_/      
    |      __|__
    |        |
    |        |
    |       
   /|\               
  / | \              
 /  |  \             
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
"""
,
"""------------------
    |        |
    |        |
    |       / \      
    |       \_/      
    |      __|__
    |        |
    |        |
    |       /        
   /|\     /         
  / | \              
 /  |  \             
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
"""
,
"""------------------
    |        |
    |        |
    |       / \      
    |       \_/      
    |      __|__
    |        |
    |        |
    |       / \      
   /|\     /   \     
  / | \              
 /  |  \             
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
"""
]
liste = []
def recherche_dans_fichier():
    
    fichier = open("mots.txt","r") # va dans mon fichier ou il y a les mots
    for ligne in fichier: # parcours les lignes du fichier txt
        ligne = ligne.replace('\n', '')
        liste.append(ligne)
    fichier.close()
    
    return liste
    
def perdu():
    print("""\033[31m _______   ________  _______   _______   __    __ 
/       \ /        |/       \ /       \ /  |  /  |
$$$$$$$  |$$$$$$$$/ $$$$$$$  |$$$$$$$  |$$ |  $$ |
$$ |__$$ |$$ |__    $$ |__$$ |$$ |  $$ |$$ |  $$ |
$$    $$/ $$    |   $$    $$< $$ |  $$ |$$ |  $$ |
$$$$$$$/  $$$$$/    $$$$$$$  |$$ |  $$ |$$ |  $$ |
$$ |      $$ |_____ $$ |  $$ |$$ |__$$ |$$ \__$$ |
$$ |      $$       |$$ |  $$ |$$    $$/ $$    $$/ 
$$/       $$$$$$$$/ $$/   $$/ $$$$$$$/   $$$$$$/  
\033[0m""")                                                  
                                                  
                                                  

def title_pendu():
    print("""\033[34m _______   ________  __    __  _______   __    __ 
|       \ |        \|  \  |  \|       \ |  \  |  |
| $$$$$$$\| $$$$$$$$| $$\ | $$| $$$$$$$\| $$  | $$
| $$__/ $$| $$__    | $$$\| $$| $$  | $$| $$  | $$
| $$    $$| $$  \   | $$$$\ $$| $$  | $$| $$  | $$
| $$$$$$$ | $$$$$   | $$\$$ $$| $$  | $$| $$  | $$
| $$      | $$_____ | $$ \$$$$| $$__/ $$| $$__/ $$
| $$      | $$     \| $$  \$$$| $$    $$ \$$    $$
 \$$       \$$$$$$$$ \$$   \$$ \$$$$$$$   \$$$$$$ 
\033[0m""")
                                                  
def termine():
    print("""\033[34m ________  ________  _______   __       __  ______  __    __  ________ 
/        |/        |/       \ /  \     /  |/      |/  \  /  |/        |
$$$$$$$$/ $$$$$$$$/ $$$$$$$  |$$  \   /$$ |$$$$$$/ $$  \ $$ |$$$$$$$$/ 
   $$ |   $$ |__    $$ |__$$ |$$$  \ /$$$ |  $$ |  $$$  \$$ |$$ |__    
   $$ |   $$    |   $$    $$< $$$$  /$$$$ |  $$ |  $$$$  $$ |$$    |   
   $$ |   $$$$$/    $$$$$$$  |$$ $$ $$/$$ |  $$ |  $$ $$ $$ |$$$$$/    
   $$ |   $$ |_____ $$ |  $$ |$$ |$$$/ $$ | _$$ |_ $$ |$$$$ |$$ |_____ 
   $$ |   $$       |$$ |  $$ |$$ | $/  $$ |/ $$   |$$ | $$$ |$$       |
   $$/    $$$$$$$$/ $$/   $$/ $$/      $$/ $$$$$$/ $$/   $$/ $$$$$$$$/ 
\033[0m""")                                                                      
                                                                       
                                                                       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def afficher_score_txt(mot_trouve, mot_total):
    if mot_total > 0:
        pourcentage = round(100*(mot_trouve/mot_total))
    else:
        pourcentage = 0
    date_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    NomFichier = 'score.txt'
    message_score = "{0} Votre score total est : {1} mots trouvés sur {2},  soit {3}%\n".format(date_time,mot_trouve, mot_total, pourcentage)
    Fichier = open(NomFichier, 'a')
    Fichier.write(message_score)
    
    
    
    Fichier.close()
        
    
    
    

    
    
    
    
    
    
def mots_aleatoires(liste_de_mots):
    
    toto = random.choice(liste_de_mots)
    liste_de_mots.remove(toto)
   
    return toto 



message = ""
def lettre_dans_tirrets(tirrets, choix, message, lettres_liste):
    
    for letter in choix:
        if letter in lettres_liste:
            message+=letter
        else:
            message += ("_ ")
    print(message)
    return message
            
            





def question(question_lettre, lettres_liste):

    while len(question_lettre) != 1:
        question_lettre = input("Veuillez entrez qu'une seule lettre -->")
    while question_lettre in lettres_liste:
        question_lettre = input("Lettre déja utilisée, veuillez en choisir une nouvelle --> ")       
    lettres_liste.append(question_lettre)
    while question_lettre == "":
        question_lettre = input("Vous devez entrer au moins un carractère")

    
def lettre_dans_mot(question_lettre, choix):
    succes = 0
    if question_lettre in choix:
        for m in choix:
            if m == question_lettre:
                succes += 1
    return succes


        
        
              

def lettre_pas_dans_mot(question_lettre, choix):
    erreurs = 0
    for p in choix:
        if p == question_lettre:
            erreurs = erreurs + 1    
            
    return erreurs

def userhelp(choix, lettres_liste):
    u = []
    for x in choix:
        if x not in lettres_liste:
            u.append(x)
    if len(u) == 0:
        return ""
    
    return random.choice(u)
        
           
                
    
            


def chargement():
    animation = "|/-\\ "

    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()


def main(message, liste):
    
    erreur_total = 0
    
    
    liste_de_mots = recherche_dans_fichier()    
    mot_total = len(liste_de_mots)
    boucle_choix = True
    mot_trouve = 0
    while boucle_choix:       
        L = []
        oui = ["oui", "Oui", "OUI", "yes", "Yes", "yeS", "YES", "ouI"]
        lettres_liste = []
        erreurs = 0
        erreurs_aide = 0
        liste_bonne_lettre = []
        succes = 0
        
        running = True
        
        choix = mots_aleatoires(liste_de_mots)
        tirrets = ["_ " *len(choix)]
        test = ("_ " * len(choix))
        print("\nTaille du mot à deviner : ", test)
        
        while running:
            
               
            
            
            question_lettre = input("\nlettre --> ")
            question(question_lettre, lettres_liste)
            

            if question_lettre not in choix:
                erreurs = erreurs +1
                erreurs_aide += 1
                erreurs +=lettre_pas_dans_mot(question_lettre, choix)
                print(dessin_pendu[erreurs])
                print("Dommage ! La lettre : ", question_lettre, "n'appartient pas au mot mystère.")
                erreur_total+=1
                print("\nVotre nombre d'erreurs est : ", erreurs, "Score : ", succes)
            
            if erreurs == 7:
                running = False
                perdu()
                print("\n")
                print("Dommage ! Vous avez perdu ! Le mot était : ","\033[91m", choix,"\033[0m" )
                
                        
                        
                    
            if erreurs_aide == 3:
                erreurs_aide = 0
                aide = input("Souhaitez vous être aidé ? (y/n)")
                if aide == "y":                    
                    
                    lettre_aide = userhelp(choix, lettres_liste)
                    print("Dans ce mot, il exite le carractère : ", lettre_aide, "!")
                              
            
            if question_lettre in choix:
                succes+=lettre_dans_mot(question_lettre, choix)
                liste_bonne_lettre.append(question_lettre)
                print(liste_bonne_lettre)
                lettre_dans_tirrets(tirrets, choix, message, lettres_liste)                
                print("\nVotre nombre d'erreurs est : ", erreurs, "Score : ", succes)
                
                if len(choix) == succes:
                    
                    print("\nBravo ! Le mot était --> ","\033[32m", choix,"\033[0m")
                    mot_trouve +=1
                    print("\nMots trouvés : ", mot_trouve)
                    
                    running = False
            if erreurs == 7 or len(choix) == succes:       
                if len(liste_de_mots) != 0:
                    mot_suivant = input("Voulez vous passer au mot suivant ? (oui/non) --> ")
                
                    if mot_suivant not in oui:
                        boucle_choix = False
                else:
                    boucle_choix = False
    afficher_score_txt(mot_trouve, mot_total)
    print("\n")
    termine()
    
title_pendu()            
print("\nBonjour, bienvenue sur le jeu du pendu !")
print("\nVeuillez choisir ce que vous souhaitez faire :")
print("-----------------------------")
print("| 1 - Jouer au pendu         |")
print("| 2 - Modifier les mots      |")
print("| 3 - Lire les règles        |")
print("| 4 - Supprimer les mots     |")
print("| q - Quitter                |")
print("------------------------------")

start = input("Votre choix --> ")
if start == "1":
    chargement()
    main(message, liste)
