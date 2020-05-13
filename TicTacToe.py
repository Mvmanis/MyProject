board=["-","-","-","-","-","-","-","-","-"]
# Global variables
game_still_going=True
current_player="x"
# who won are tie
winner=None

def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2]+"          1 | 2 |3")
    print(board[3] + " | " + board[4] + " | " + board[5]+"          4 | 5 |6")
    print(board[6] + " | " + board[7] + " | " + board[8]+"          7 | 8 |9")
    print("\n")

def play_game():
    # global winner
    # global game_still_going
    # global Current_player
    #Display initial board
    display_board()

    # display_board()
    while game_still_going:
        handle_turn(current_player)
        cheak_if_game_over()
        flip_player()
    if winner=="x" or winner=="o":
        print(winner+" is winner.")
    elif winner==None:
        print("Tie.")
	

def handle_turn(player):
    print(player+"'s turn")
    # print("\n")
    position = (input("Enter a position from 1-9:"))
    valid=False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position=input("Enter the position again invalid postion: ")
        position = int(position) - 1
        if board[position]=="-":
            valid=True
        else:
            print("You can't go there")
    board[position]=player
    display_board()

def cheak_if_game_over():
    cheak_for_winner()
    cheak_if_tie()

def flip_player():
    global current_player
    if current_player=="x":
        current_player="o"
    elif current_player=="o":
        current_player="x"
    return

def cheak_for_winner():
    global winner
    # cheak_rows
    row_winner=cheak_rows()

    # cheak_column
    col_winner=cheak_column()

    # cheak_diagonal
    dia_winner=cheak_diagonal()
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif dia_winner:
        winner = dia_winner
    else:
        winner =None

def cheak_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False
        return True
    else:
        return False

def cheak_rows():

    global game_still_going
    row_1=board[0]==board[1]==board[2]!="-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
       game_still_going=False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def cheak_column():
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        game_still_going=False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return None

def cheak_diagonal():
    global game_still_going
    dia_1 = board[0] == board[4] == board[8] != "-"
    dia_2 = board[6] == board[4] == board[2] != "-"
    if dia_1 or dia_2 :
        game_still_going=False
    if dia_1:
        return board[0]
    elif dia_2:
        return board[6]
    else:
        return None

play_game()
a=input()