import math
import random

size = 4

def myTicTacToe(grille, monSymbole):

    autreSymbole = -monSymbole
    x = 0
    y = 0
    myMove =0               # nombre de notre symbole existe dans un motif de victoire
    sonMove =0

    # rechercher sur toutes les lignes

    for i in range(0, 4):
        x = i
        for j in range(0, 4):
            y = j
            if grille[x][y] == monSymbole:  # la première étape est de chercher un motif de victoire qui existe déjà 3 monSymbole
                myMove += 1  # s'il existe, on renvoie la position de case vide dans ce motif
                i += 1
                j += 1
            if myMove == 3 and grille[x][y] == 0:
                # print('myMove sur la ligne = 3', x, y)
                return (x, y)
            if grille[x][y] == autreSymbole:  # la deuxième étape est de chercher un motif de victoire qui existe déjà 3 symboles de notre adversaire
                sonMove += 1  # s'il existe, on renvoie la position de case vide dans ce motif
                i += 1
                j += 1
            if sonMove == 3 and grille[x][y] == 0:
                # print('sonMove sur la ligne = 3', x, y) on fait pareil pour chaque motif de victoire
                return (x, y)

    # Rechercher sur toutes les colonnes

    for j in range(0, 4):
        x = j
        for i in range(0, 4):
            y = i
            if grille[x][y] == monSymbole:
                myMove += 1
                i += 1
                j += 1
            if myMove == 3 and grille[x][y] == 0:
                # print('myMove sur une colonne = 3', x, y)
                return (x, y)
            if grille[x][y] == autreSymbole:
                sonMove += 1
            if sonMove == 3 and grille[x][y] == 0:
                # print('sonMove sur une colonne = 3', x, y)
                return (x, y)

    # Rechercher sur une diagonale

    for j in range(0,4):
        x = j
        y = j
        if grille[x][y] == monSymbole :
            myMove += 1
            j += 1
        if myMove == 3 and grille[x][y] == 0:
            # print('myMove sur une diagonale = 3', x, y)
            return (x, y)
        if grille[x][y] == autreSymbole:
            sonMove += 1
            j += 1
        if sonMove == 3 and grille[x][y] == 0:
            # print('sonMove sue une diagonale = 3', x, y)
            return (x, y)

    # Rechercher sur l'autre diagonale

    for j in range(0,4):
        x = j
        y = 3-j
        if grille[x][y] == monSymbole :
            myMove += 1
            j += 1
        if myMove == 3 and grille[x][y] == 0:
            # print("myMove sur l'autre diagonale = 3", x, y)
            return (x, y)
        if grille[x][y] == autreSymbole:
            sonMove += 1
            j += 1
        if sonMove == 3 and grille[x][y] == 0:
            # print("sonMove sur l'autre diagonale = 3", x, y)
            return (x, y)

    # recherche sur tous les carrés ( un peu bizarre )

    for i in range(0,2):
        for j in range(0,2):
            x = i
            y = j
            if grille[x][y] == monSymbole or grille[x+1][y] == monSymbole or grille[x][y+1] == monSymbole or grille[x+1][y+1] == monSymbole:
                myMove += 1
                i += 1
                j += 1
            if myMove == 3 :
                if grille[x][y] == 0:
                    print('myMove sur une carré = 3', (x, y))
                    return (x, y)
                elif grille[x+1][y] == 0:
                    print('myMove sur une carré = 3', (x+1, y))
                    return (x+1, y)
                elif grille[x][y+1] == 0:
                    print('myMove sur une carré = 3', (x, y+1))
                    return (x, y+1)
                elif grille[x+1][y+1] == 0:
                    print('myMove sur une carré = 3', (x+1, y+1))
                    return (x+1, y+1)
            if grille[x][y] == autreSymbole or grille[x+1][y] == autreSymbole or grille[x][y+1] == autreSymbole or grille[x+1][y+1] == autreSymbole:
                sonMove += 1
            if sonMove == 3:
                if grille[x][y] == 0:
                    print('sonMove sur une carré = 3', (x, y))
                    return (x, y)
                elif grille[x+1][y] == 0:
                    print('sonMove sur une carré = 3', (x+1, y))
                    return (x+1, y)
                elif grille[x][y+1] == 0:
                    print('sonMove sur une carré = 3', (x, y+1))
                    return (x, y+1)
                elif grille[x+1][y+1] == 0:
                    print('sonMove sur une carré = 3', (x+1, y+1))
                    return (x+1, y+1)

    # Nos differentes stratégies gagnantes
    
    priorité_0 = [[2,2],[3,2],[2,3],[3,3]]

    priorité_1 = [[1,1],[1,2],[2,1]]

    priorité_2 = [[1,0],[2,0],[0,1],[0,2],[1,3],[3,1]]

    priorité_3 = [[0,0],[0,3],[3,0]]

    for [x,y] in priorité_0:
           if grille[x][y] == 0:
               # print("case vide en priorité 1, à la position ", (x, y))
               return (x,y)
    for [x,y] in priorité_1:
           if grille[x][y] == 0:
               # print("case vide en priorité 1, à la position ", (x, y))
               return (x,y)
    for [x,y] in priorité_2:
           if grille[x][y] == 0:
               # print("case vide en priorité 2, à la position ", (x, y))
               return (x,y)
    for [x,y] in priorité_3:
           if grille[x][y] == 0:
               # print("case vide en priorité 3, à la position ", (x, y))
               return (x,y)
    return (x,y)

def check(tab):
    global sum
    sum = 0
    motif = 0

    global finished
    finished = False
    global winner
    winner = -1


    #check lines
    for i in range(0,4):
        sum = 0
        for j in range(0,4):
            sum = sum + tab[i][j]
        #print("lines" + str(sum))
        if math.fabs(sum) == 4:
            motif = sum

    #check columns
    for i in range(0,4):
        sum = 0
        for j in range(0,4):
            sum = sum + tab[j][i]
        #print("columns" + str(sum))
        if math.fabs(sum) == 4:
            motif = sum

    #check diags
    sum = 0
    for j in range(0,4):
        sum = sum + tab[j][j]
    if math.fabs(sum) == 4:
        motif = sum

    sum = 0
    for j in range(0,4):
        sum = sum + tab[j][3 - j]
    if math.fabs(sum) == 4:
        motif = sum

    #check squares
    for i in range(0,2):
        for j in range(0,2):
            sum = tab[i][j]+tab[i+1][j]+tab[i][j+1]+tab[i+1][j+1]
            if math.fabs(sum) == 4:
                motif = sum

    if motif == 4:
        finished = True
        winner = 1
    elif motif == -4:
        finished = True
        winner = -1
    else :
        finished = True
        winner = 0
        for i in range(0,4):
            if tab[i][j] == 0:
                finished = False

    #print(str(winner)+" "+str(finished))
    return (winner, finished)


def tictactoeRandom(grille, monSymbole) :
    x = random.randint(0,(size - 1))
    y = random.randint(0,(size - 1))

    #print(grille[x][y])

    while (grille[x][y] == monSymbole or (grille[x][y] + monSymbole) == 0):
        x = random.randint(0, (size - 1))
        y = random.randint(0, (size - 1))

    return (x,y)

def affecterSymbole(grille, monSymbole, x, y):
    #print(grille)
    #print(x, y)
    grille[x][y] = monSymbole
    #print(grille)

def affichage(grille):
    for i in range(0, size):
        ch = ""
        for j in range(0, size):
            ch += str(grille[i][j])+" "
        print(ch)
    print()




grille = [0]*size
for i in range(size):
        grille[i] = [0] * size

affichage(grille)

winner = 0
finished = False

while (winner == 0 or finished == False):
    monSymbole = -1
    #print(grille)
    (x,y) = tictactoeRandom(grille, monSymbole)

    affecterSymbole(grille, monSymbole, x, y)
    #print(grille)

    print("Dummy player")
    affichage(grille)
    (winner, finished) = check(grille)

    if (winner == 0 or finished == False):
        monSymbole = 1
        (x,y) = myTicTacToe(grille, monSymbole)
        affecterSymbole(grille, monSymbole, x, y)
        (winner, finished) = check(grille)

        print("Student player")
        affichage(grille)