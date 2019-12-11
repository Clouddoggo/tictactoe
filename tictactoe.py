import os
import sys

# board = ['' for x in range(9)]
board = ['', '', '', '', '', '', '', '', '']
clear = lambda: os.system('cls')

def findWinner(ls):
    for i in range(0, len(ls) - 2, 3):
        if (ls[i] == board[i + 1] == ls[i + 2] and ls[i] != ''):
            return ls[i]
    for i in range(3):
        if (ls[i] == ls[i + 3] == ls[i + 6] and ls[i] != ''):
            return ls[i]
    if ((ls[0] == ls[4] == ls[8] and ls[0] != '') or 
        (ls[2] == ls[4] == ls[6] and ls[2] != '')):
        return ls[4]
    return 'tie'
        

def clearBoard():
    global board
    board = ['', '', '', '', '', '', '', '', '']

def displayBoard(ls):
    print('Board positions:')
    for i in range(0, len(ls) - 2, 3):
        print(f'{i + 1} | {i + 2} | {i + 3}            {ls[i]} | {ls[i + 1]} | {ls[i + 2]}')
        if (i < len(ls) - 3):
            print('----------           ----------')

def getStatus():
    contPlaying = input('Would you like to start a new game?\nEnter y if yes: ')
    contPlaying = contPlaying.lower()
    if (contPlaying == 'y'):
        print('Starting a new game. Please wait')     
        clearBoard()
        clear()
        return True
    else:
        print('Thank you for playing!')
        clearBoard()
        return False
    

def getInput():
    print('Welcome to Tic-Tac-Toe!')
    user = input('Who do you want to be? Player X or O? Enter X or O: ')
    user = user.upper()
    if (user != 'X' and user != 'O'):
        print("Please enter X or O")
        getInput()
    else:
        count = 0
        global board
        displayBoard(board)
        while (True):
            print(f'Player {user} please enter a board position from 1 to 9:')
            number = input('')
            number = int(number)
            if (number < 1 or number > 9):
                print('Sorry, that was an invalid number!')
                continue
            elif (board[number - 1] != ''):
                print('This space has been used.')
                continue
            else:
                count += 1
                board[number - 1] = user
                if (user == 'X'):
                    user = 'O'
                else:
                    user = 'X'
            clear()
            displayBoard(board)
            winner = findWinner(board)
            if (winner != 'tie'):
                print(f'Congratulations, Player {winner}')
                if (getStatus()):
                    getInput()
                else:
                    break
            if (count == 9):
                winner = findWinner(board)
                if (winner == 'tie'):
                    print(f'It\'s a tie!')
                else:
                    print(f'Congratulations, Player {winner}')
                if (getStatus()):
                    getInput()
                else:
                    print('else')
                    break
                      
getInput()