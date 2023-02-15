import random
import time


# Set some colors to identify the two symbols
red = "\033[31m"
green = "\033[32m"
reset = "\033[39m"  # Rest back to gray

def _init_game():
    global user, machine, cells, available_cells, board, symbol

    # init scores
    user = {'rows':[0, 0, 0], 'cols':[0, 0, 0], 'diag':[0, 0]}
    machine = {'rows':[0, 0, 0], 'cols':[0, 0, 0], 'diag':[0, 0]}


    # Map the cells' idxs to numbers
    cells = {'1':[0,0], '2':[0,1], '3':[0,2], '4':[1,0], '5':[1,1], '6':[1,2], '7':[2,0], '8':[2,1], '9':[2,2]}

    available_cells = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    board = [['1','2','3'],['4','5','6'],['7','8','9']]   # Give each cell a number, so it'll be easy to choose (for printing)

    symbol = {'user': '', 'machine': ''}  # who is X and who is O


def print_board(board):
    print('    +-----+-----+-----+')
    for r in board:
        print(f'    |  {r[0]}  |  {r[1]}  |  {r[2]}  |')
        print('    +-----+-----+-----+')


def start():
    global turn
    
    # Call _init_game to initiate the variables
    _init_game()

    print(" Hello! Tic Tac Toe ".center(40, '*'))
    print(" ... New game ... ".center(40))

    who_start = ' '  # Can be only 1 or 0
    while who_start not in '10':
        who_start = input("Press '1' if you would like to start, or '0' so I will start: ")
    
    user_xo = ' '  # Can be only X or O
    while user_xo.upper() not in 'XO':
        user_xo = input("Would you like to play with 'X' or 'O? ")

    # Set the first turn
    if who_start == '1':
        turn = 'user'
    else:
        turn = 'machine'


    # Set the symbols with differnt color
    if user_xo.upper() == 'X':
        symbol['user'] = red + 'X' + reset
        symbol['machine'] = green + 'O' + reset
    else:
        symbol['user'] = green + 'O' + reset
        symbol['machine'] = red + 'X' + reset

    print_board(board)


'''
After ech turn, update the bpard and print it.
'''
def update_board(cell, symbol):
    r, c = cells[cell]
    board[r][c] = symbol

    print_board(board)


'''
After echa turn, upded the score for the current player.
player: the dictionary that represents the scores for the current player.
'''
def update_score(cell, player):
    r,c = cells[cell]

    player['rows'][r] += 1
    player['cols'][c] += 1
    
    if r==0 and c ==0:
        player['diag'][0] += 1
    elif r==0 and c==2:
        player['diag'][1] += 1
    elif r==2 and c==0:
        player['diag'][1] += 1
    elif r==2 and c==2:
        player['diag'][0] += 1
    elif r==1 and c==1:
        player['diag'][0] += 1
        player['diag'][1] += 1


'''
Iterate over the dic scores for both players; machine and user to check for a winner.
Check the sum in rows, cols, and diagonals.
'''
def find_winner():
    for _, scores in user.items():
        if any(s == 3 for s in scores):
            print("You Won !!!")
            #winner = True
            return 'user'

    for _, scores in machine.items():
        if any(s ==  3 for s in scores):
            print("I won !!!")
            #winner = True
            return 'machine'

'''
Play the turn:
    - If it's the user's turn:
        - Get the desired cell and check if it's valid, othewise keep asking for a valid cell.
    - If it's the machine's turn:
        ***********************************
        -  *** FOR NOW IT IS RANDOM CHOICE FROM THE available_cells. BUT IT WILL BE MODIFIED TO USE THE MINMAX ALGORITHM. ***
        ***********************************
'''
def play_turn(turn):
    if turn == 'user':
        s = symbol['user']
        score = user

        # Read input from user and check if it's valid
        print("Your Turn ...")
        cell = input("Choose a cell: ")

        while cell not in available_cells:
            print(f"Cell {cell} is not available.")
            cell = input("Please select one of the empty cells: ")

    else:
        #  ***** THIS PART WILL BE MODIFIED ******
        s = symbol['machine']
        score = machine

        print("My Turn ...")
        # Wait for two seconds
        time.sleep(2)
        # Machine will play
        cell = random.choice(available_cells)


    # After getting a valid cell, remove it from the list of available_cells
    available_cells.remove(cell)

    # Update the board and the score
    update_board(cell, s)
    update_score(cell, score)


'''
Know whose turn is next
'''
def whose_turn(crnt_turn):
    if crnt_turn == 'machine':
        return 'user'
    else:
        return 'machine'



start()

while available_cells:
    play_turn(turn)
    winner = find_winner()
    turn = whose_turn(turn)

    if winner:
        break

if not winner:
    print("Draw")

