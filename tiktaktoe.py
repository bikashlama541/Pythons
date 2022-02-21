#----- Global Variables ----

#Game board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]  #yeslai list banayo

# If game is still game_still_going
game_still_going = True

#Who won? or tie?
winner = None

# whos turn is it?
current_player = "X"
#aba board lai display geram


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


#Game start garne function banam
def playgame():

    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
       print("Tie.")


def handle_turn(player):
    #Check if input is correct
    print (player + "'s turn.'")
    position = input("Choose a position from 1 to 9: ")

    valid = False
    
    while not valid:
      while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Choose a position from 1 to 9: ")
    position = int(position) - 1  #-1 garnu ko kararn chai number milauna

    if board[position] != "-":
      print("You can't go there. Go again")

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    global winner #bahira bata lerako, ani pachi set garna


    #check rows 
    row_winner = check_rows()
    #check colums
    column_winner = check_colums()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
      #there was a winner
      winner = row_winner
    elif column_winner:
      #there was a winner
      winner = column_winner
    elif diagonal_winner:
      #there was a winner
      winner = diagonal_winner
    else:
      winner = None  

    return

def check_rows():
  # Set uup global variables
  global game_still_going
  #sab equal tara - vayena vane , natra program first mai dhalcha
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  #If any row does have match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  #Return the winner (X or O)
  if row_1:
    return board[0]
  if row_2:
    return board[3]
  if row_3:
    return board[6]  
  return

def check_colums():
  # Set uup global variables
  global game_still_going
  #sab equal tara - vayena vane , natra program first mai dhalcha
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  #If any row does have match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  #Return the winner (X or O)
  if column_1:
    return board[0]
  if column_2:
    return board[1]
  if column_3:
    return board[2]  
  return

def check_diagonals():
  # Set uup global variables
  global game_still_going
  #sab equal tara - vayena vane , natra program first mai dhalcha
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  #If any row does have match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  #Return the winner (X or O)
  if diagonal_1:
    return board[0]
  if diagonal_2:
    return board[2] 
  return
  


def check_if_tie():
  global game_still_going
  if "-" not in board:
      game_still_going = False
  return


def flip_player():
    #Change the player
    global current_player
    if current_player == "X":
      current_player = "O"
    elif current_player == "O":
      current_player = "X"
    return


playgame()
