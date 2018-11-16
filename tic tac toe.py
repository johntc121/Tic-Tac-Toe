row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]

choices = []

def getInput():
    userInput = input("Pick an open number between 1-9: ")
    return userInput

def placeInput(getInput, char):
    if int(getInput) <= 3:
        row1[int(getInput)-1] = char
    elif int(getInput) <= 6:
        row2[int(getInput)-4] = char
    elif int(getInput) <= 9:
        row3[int(getInput)-7] = char

    choices.append(getInput)

def printBoard():
    pRow1 = "|"
    pRow2 = "|"
    pRow3 = "|"


    for slot in row1:
        pRow1 = pRow1 + str(slot) + "|"
    for slot in row2:
        pRow2 = pRow2 + str(slot) + "|"
    for slot in row3:
        pRow3 = pRow3 + str(slot) + "|"

    print("--------")
    print(pRow1)
    print(pRow2)
    print(pRow3)

def playGame(player):
    placeInput(getInput(), player)


def checkForWin():
    #check for across
    if row1[0] == row1[1] and row1[0] == row1[2]:
        print(row1[0] + " is the winner!")
        return True
    elif row2[0] == row2[1] and row2[0] == row2[2]:
        print(row2[0] + " is the winner!")
        return True
    elif row3[0] == row3[1] and row3[0] == row3[2]:
        print(row3[0] + " is the winner!")
        return True

    #Check for up and down
    elif row1[0] == row2[0] and row1[0] == row3[0]:
        print(row1[0] + " is the winner!")
        return True
    elif row1[1] == row2[1] and row1[1] == row3[1]:
        print(row1[1] + " is the winner!")
        return True
    elif row1[2] == row2[2] and row1[2] == row3[2]:
        print(row1[2] + " is the winner!")
        return True

    #check diagonal
    elif row1[0] == row2[1] and row1[0] == row3[2]:
        print(row1[0] + " is the winner!")
        return True
    elif row1[2] == row2[1] and row1[2] == row3[0]:
        print(row1[2] + " is the winner!")
        return True

    else:
        return False

def game():
    gameTurns = 0
    while gameTurns < 9:
        printBoard()
        player = 'X'
        playGame(player)
        printBoard()
        if checkForWin() is True:
            return
        if (len(choices) == 9):
            print("Cats Game. No Winner")
            return
        player2 = 'O'
        playGame(player2)
        printBoard()
        if checkForWin() is True:
            return
        gameTurns += 2


game()
