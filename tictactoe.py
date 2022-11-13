#-------Global Variables--------

#game board
board = ["-", "-", "-"
    , "-", "-", "-",
         "-", "-", "-"]

#if game is still going
game_still_going = True

#winner or tie
winner = None

#whose turn is it
current_player = "X"

#prints board to the screen
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
display_board()

def play_game():
    # displays the initial board
    display_board()

#loops that takes turn over and over again till someone win
    while game_still_going:
         #handles turn
         handle_turn(current_player)

     # check_if game is over
         check_if_game_finished()

      #change player
         flip_player()
    #we have a winner
         if winner == "X" or winner =="O":
           print(winner + " won.")
         elif winner == None:
               print("Tie.")

def handle_turn(player):

    print(player + "'s turn.")
    position = input("choose a position from 1-9: ")

    

#so theres not out of bound numbers in the board
    while position not in ["1","2","3","4","5","6","7","8","9"]:
        position = input("invalid input. choose a position 1-9")
    position = int(position) - 1
# so cant duplicate input in the same place

    if board [position] == "-":
        print ("you cant go there ")

    board[position] = player

    display_board()

 #   position = input("choose a position from 2-9: ")
  #  position = int(position) - 2

   # board[position] = "o"
    #display_board()

def check_if_game_finished():
    #check for winner
    check_if_win()
    #check for tie
    check_if_tie()

def check_if_win():

    #set global winner
    global winner
    #check row
    row_winner = check_rows()
    #check column
    column_winner = check_columns()
    #check diagonal
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global game_still_going 
    #check if all rows have all the same value
    row_1 = board[0] == board[1]==  board[2] !="-"
    row_2 = board[3] == board[4] == board[5] !="-"
    row_3 = board[6] == board[7] == board[8] !="-"

    #if rows had match print win
    if row_1 or row_2 or row_3 :
        game_still_going = False

    if row_1:
            return board[0]
    elif row_2:
            return board[3]
    elif row_3:
        return board[6]
        return

def check_columns():
    #sets up global variable
    global game_still_going
    #check if any column have all the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    #if any column does have man flags that there is a winner
    if column_1 or column_2 or column_3:
        game_still_going = False
        if column_1:
           return board[0]
        elif column_2:
          return  board[1]
        elif column_3:
            return board[2]
            return

def check_diagonals():
    global game_still_going
    #check if any diagonal have all same value
    diagonal_1 = board[0] == board[4] == board[8] !="-"
    diagonal_2 = board[6] == board[4] == board[2] !="-"
    #if any diagonals have a match flag there is a  winner
    if diagonal_1 or diagonal_2:
        game_still_going = False
        if diagonal_1:
            return board[0]
        elif diagonal_2:
            return board[6]
        return
    #check row
    #check column

def check_if_tie():
    global  game_still_going
    #if all the spaces are filled and hasn't flagged row/column/diagonal winner then it is a tie
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player
    #checks player from x to o
    if current_player == "X":
        current_player = "O"

    elif current_player =="O":
        current_player = "X"
    return



play_game()