def display_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def player_assignment():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def player_input(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def player_marker(board,pos,marker):
    board[pos]=marker
    
def win_check(board,marker):
    return((board[1]== marker and board[2] == marker and board[3] == marker)or#right 1st row
    (board[4]== marker and board[5] == marker and board[6] == marker)or#right 2nd row
    (board[7]== marker and board[7] == marker and board[9] == marker)or#right 3rd row
    (board[1]== marker and board[4] == marker and board[7] == marker)or#down 1st col
    (board[2]== marker and board[5] == marker and board[8] == marker)or#down 2nd col
    (board[3]== marker and board[6] == marker and board[9] == marker)or#down 3rd col
    (board[7]== marker and board[5] == marker and board[3] == marker)or#diagonal
    (board[9]== marker and board[5] == marker and board[1] == marker))#diagonal
    
def space_check(board, position):
    
    return board[position] == ' '

def fullboard_spacecheck(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

print('Welcome to Tic-Tac-Toe')


while True:
    
    the_board = [' ']*10
    p1,p2= player_assignment()
    turn = choose_first()
    print ('{} goes first!'.format(turn))

    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
    
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_input(the_board)
            player_marker(the_board,position,p1)
        
            if win_check(the_board,p1) == True:
                display_board(the_board)
                print('Congratulations! You have won the game!')
                game_on = False
            
            else:
                if fullboard_spacecheck(the_board) == True:
                    display_board(the_board)
                    print('The game is a draw!')
                    game_on = False
                else:
                    
                    turn = 'Player 2'
                    
        else:
        
            display_board(the_board)
            position = player_input(the_board)
            player_marker(the_board,position, p2)

            
            if win_check(the_board, p2):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if fullboard_spacecheck(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break