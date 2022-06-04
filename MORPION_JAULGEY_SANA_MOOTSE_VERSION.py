def jeux(morpion, nom, symbole, V):
    Xsaisie = int(input('Quelle ligne ? '))
    while Xsaisie > 3:
        Xsaisie = int(input('Erreur, quelle ligne ? '))
    Ysaisie = int(input('Quelle colonne ? '))
    while Ysaisie > 3:
        Ysaisie = int(input('Erreur, quelle ligne ? '))
    Xsaisie = Xsaisie -1
    Ysaisie = Ysaisie -1
    if morpion[Xsaisie][Ysaisie] == " ":
        morpion[Xsaisie][Ysaisie]
        print (nom, "a saisi", symbole, "en", (Xsaisie+1, Ysaisie+1))
        morpion[Xsaisie][Ysaisie] = symbole
    else:
        print ("Impossible, case occupée")
    
    print ("----------")
    print (morpion[0][0], "|", morpion[0][1], "|", morpion[0][2] )
    print ("----------")
    print (morpion[1][0], "|", morpion[1][1], "|", morpion[1][2] )
    print ("----------")
    print (morpion[2][0], "|", morpion[2][1], "|", morpion[2][2] )
    print ("----------")
    V = victoire(nom, morpion, V, Xsaisie, Ysaisie, symbole)
    return morpion, V


def victoire(nom, morpion, V, Xsaisie, Ysaisie, symbole):
    if morpion[Xsaisie][0] == symbole and morpion[Xsaisie][1] == symbole and morpion[Xsaisie][2] == symbole:
        print(nom, 'a gagné !!')
        V = 1
    elif morpion[0][Ysaisie] == symbole and morpion[1][Ysaisie] == symbole and morpion[2][Ysaisie] == symbole:
        print(nom, 'a gagné !!')
        V = 1
    elif morpion[0][0] == symbole and morpion[1][1] == symbole and morpion[2][2] == symbole:
        print(nom, 'a gagné !!')
        V = 1
    elif morpion[0][2] == symbole and morpion[1][1] == symbole and morpion[2][0] == symbole:
        print(nom, 'a gagné !!')
        V = 1
    elif morpion[0][0] != " " and morpion[0][1] != " " and morpion[0][2] != " " and morpion[1][0] != " " and morpion[1][1] != " " and morpion[1][2] != " " and morpion[2][0] != " " and morpion[2][1] != " " and morpion[2][2] != " ":
        print ("Match nul, personne n\'a gagné !")
        V=1
    else:
        V = 0
    return V


def debt(nom1, nom2, u1, u2, V):
    debut = input('Qui commence ? (J1 / J2) :')
    if(debut == 'J1'):
        u1 = int(1)
        u2 = int(0)
    elif(debut == 'J2'):
        u1 = int(0)
        u2 = int(1)
    else: 
        print("Valeur incorrecte, merci de ressaisir la valeur : ")
        debt(nom1, nom2, u1, u2, V)
    u1, u2, V = switch(u1, u2, nom1, nom2, morpion, V)
    print ("\tX est le symbole du joueur 1")
    print ("\tO est le symbole du joueur 2")
    return u1, u2

def switch(u1, u2, nom1, nom2, morpion, V):
    if(V== 0):
        if u1 == 1:
            symbole = 'X'
            morpion, V =jeux(morpion, nom1, symbole, V)
            u1=int(0)
            u2=int(1)
        elif u2 == 1:
            symbole = 'O'
            morpion, V =jeux(morpion, nom2, symbole, V)
            u1=int(1)
            u2=int(0)
    elif(V==1):
        print('Fin du jeu')
    return u1, u2, V
        


###### JEU ######
morpion = [[" " for i in range(3)] for i in range(3)]
nom1 = input('Nom d\'utilisateur 1 : ')
nom2 = input('Nom d\'utilisateur 2 : ')
score1 =0
score2 = 0
u1 = 0
u2 = 0
V = 0
u1, u2 = debt(nom1, nom2, u1, u2, V)
while(V == 0):
    u1, u2, V = switch(u1, u2, nom1, nom2, morpion, V)
