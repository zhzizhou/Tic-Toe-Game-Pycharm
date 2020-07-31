import random
import pylint

# display board function to display the game board
def display_board(board):
    while len(board) != 9:
        return "invalid keyboard input"
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# generate the first input of the program
# asking the choice of the firstplayer to startoff
def player_input():
    answer = 'nothing'
    while answer != 'X' and answer != 'O':
        answer = input("player1: what is your choice (X or O)?")
    return answer


# To place the desired marker(X or O) in the desired position
def place_marker(board, marker, position):
    if position > 9:
        return "please choose a desired position(number 1-9)"

    board[position - 1] = marker


# win_check to check if condition is met to win the game
def win_check(board, mark):
    if board[0] == board[1] == board[2] == mark:
        return True
    elif board[0] == board[3] == board[6] == mark:
        return True
    elif board[0] == board[4] == board[8] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[3] == board[4] == board[5] == mark:
        return True
    elif board[6] == board[7] == board[8] == mark:
        return True
    elif board[2] == board[4] == board[6] == mark:
        return True
    return False


# use random function to decide which player go first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player B'
    else:
        return 'Player A'


# function check if the desired place is occupied
def space_check(board, position):
    if board[position - 1] == ' ':
        return True
    return False


# if the board is full, then early win_check will be needed to determine win
def full_board_check(board):
    for i in board:
        if i == ' ':
            return False
    return True


# most important working function
# check the validation of  the player's choice and return their valid choice
def player_choice(board, player):
    choice = "nothing"
    condition = True
    while condition:
        while (choice not in range(1, 10)):
            choice = int(input(f"{player} please enter your next position(number 1-9)"))

        if space_check(board, choice):
            condition = False
        else:
            print("Invalid input! That spot is been occupied!")
            choice = int(input(f"{player} please enter your next position(number 1-9)"))
    return choice


# final function to ask if the player want to player again
def replay():
    choice = "nothing"
    while choice != 'Y' and choice != 'N':
        choice = input("Do you want to play again?(Y/N)")
    if choice == 'Y':
        return True
    else:
        return False





def main():
    # Main program proceed
    print('Welcome to Tic Tac Toe!')

    # use double while loop to create looping environment
    # use break as the only breakpoint to break the outer loop
    while True:
        # Set the game up here
        # labelling each player's choice
        playerA_choice = player_input()
        if playerA_choice == 'X':
            playerB_choice = 'O'
        else:
            playerB_choice = "X"

        # here to define the first player or second player by order
        firstplayer = choose_first()
        print(f"{firstplayer} will go first")

        # set up the empty board and display the empty board
        game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        display_board(game_board)

        # the condition of whether there is a win determine the inner while loop running
        win = False
        # while game_on:
        while win == False:

            # firstplayer Turn --------------------------------------------------------------
            if firstplayer == 'Player A':
                firstplayerchoice = playerA_choice
            else:
                firstplayerchoice = playerB_choice

            # check if the board is full and make early win_check
            if full_board_check(game_board):
                if win_check(game_board, firstplayerchoice):
                    print(f"{firstplayer} you won")
                    win = True
                    break
            # if the board is not full then we can place the choice into desired location
            place_marker(game_board, firstplayerchoice, player_choice(game_board, firstplayer))
            display_board(game_board)

            # check win condition
            if win_check(game_board, firstplayerchoice):
                win = True
                print(f"{firstplayer} you won")
                break

            # secondplayer turn --------------------------------------------------------------
            if firstplayer == 'Player A':
                secondplayer = 'Player B'
                secondplayerchoice = playerB_choice
            else:
                secondplayer = 'Player A'
                secondplayerchoice = playerA_choice

            # check if the board is full and make early win_check
            if full_board_check(game_board) == True:
                if win_check(game_board, secondplayerchoice) == True:
                    print(f"{secondplayer} you won!")
                    win = True
                    break
            place_marker(game_board, secondplayerchoice, player_choice(game_board, secondplayer))
            display_board(game_board)

            if win_check(game_board, secondplayerchoice) == True:
                win = True
                print(f"{firstplayer} you won")
                break

        # ask whether the player want to play again?
        # if not then breakout the outer while loop to terminal the program
        if not replay():
            break



if __name__ == '__main__':
    main()
