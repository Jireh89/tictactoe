import sys, os
board = ["_", "_", "_", 
"_", "_", "_",
"_", "_", "_"]

def display():
    print board[0] + " | " + board[1] + " | " + board[2] + " |   0 | 1 | 2 |"
    print board[3] + " | " + board[4] + " | " + board[5] + " |   3 | 4 | 5 |"
    print board[6] + " | " + board[7] + " | " + board[8] + " |   6 | 7 | 8 |"

def checkWin():
    win = False
    # horizontal check
    if(not board[0] == "_" or not board[1] == "_" or not board[2] == "_") and (board[0] == board[1] == board[2]):
        win = True
    elif(not board[3] == "_" or not board[4] == "_" or not board[5] == "_") and (board[3] == board[4] == board[5]):
        win = True
    elif(not board[6] == "_" or not board[7] == "_" or not board[8] == "_") and (board[6] == board[7] == board[8]):
        win = True
    # vertical check
    elif(not board[0] == "_" or not board[3] == "_" or not board[6] == "_") and (board[0] == board[3] == board[6]):
        win = True
    elif(not board[1] == "_" or not board[4] == "_" or not board[7] == "_") and (board[1] == board[4] == board[7]):
        win = True
    elif(not board[2] == "_" or not board[5] == "_" or not board[8] == "_") and (board[2] == board[5] == board[8]):
        win = True
    # diagonal check
    elif(not board[0] == "_" or not board[4] == "_" or not board[8] == "_") and (board[0] == board[4] == board[8]):
        win = True
    elif(not board[6] == "_" or not board[4] == "_" or not board[2] == "_") and (board[6] == board[4] == board[2]):
        win = True
    
    if not win:
        global winner
        winner = "no one"
        win = True
        for x in range(0, 9):
            if board[x] == "_":
                win = False

    return win

def player1():
    user_number = raw_input()
    try:
        s = int(user_number)

        if s > -1 and s < 9 and board[s] == "_":
            board[s] = "X"
        else:
            print "Invalid Input"
            display()
            player1() 
    except ValueError:
        sys.exit()

def player2():
    for x in range(0, 9):
        if board[x] == "_":
            board[x] = "O"
            if checkWin():
                return
            else:
                board[x] = "_"                
    
    for x in range(0, 9):
        if board[x] == "_":
            board[x] = "X"
            if checkWin():
                board[x] = "O"
                return
            else:
                board[x] = "_" 
    
    if board[4] == "_":
        board[4] = "O"
    elif board[8] == "_":
        board[8] = "O"
    elif board[2] == "_":
        board[2] = "O"
    elif board[0] == "_":
        board[0] = "O"
    elif board[6] == "_":
        board[6] = "O"
    elif board[1] == "_":
        board[1] = "O"
    elif board[3] == "_":
        board[3] = "O"
    elif board[5] == "_":
        board[5] = "O"
    elif board[7] == "_":
        board[7] = "O"      

def check():
    if checkWin():
        display()
        print winner + " win"
        sys.exit()

while True:
    os.system('cls')
    display()
    player1()
    winner = "player1"
    check()
    player2()
    winner = "player2"
    check()