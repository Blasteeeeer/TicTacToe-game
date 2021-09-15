board = [" " for i in range(0, 9)]


def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def player_move(icon):
    flag = 1

    while flag:
        choice = int(input("{} Player enter your move (between 1-9): ".format(icon)).strip())
        if choice not in range(1, 10):
            print("Please enter the proper value ")
            flag = 1
        elif board[choice - 1] == " ":
            board[choice - 1] = icon
            flag = 0
        else:
            print("That move is not possible!")
            flag = 1


def is_victory(icon):
    if (board[0] == board[1] == board[2] == icon) or (board[3] == board[4] == board[5] == icon) or (board[6] == board[7] == board[8] == icon) or (board[0] == board[3] == board[6] == icon) or (board[1] == board[4] == board[7] == icon) or (board[2] == board[5] == board[8] == icon) or (board[0] == board[4] == board[8] == icon) or (board[2] == board[4] == board[6] == icon):
        return True
    else:
        return False


def is_draw():
    if " " not in board:
        return True
    else:
        return False


print_board()
while True:
    player_move('X')
    print_board()
    if is_victory('X'):
        print("Congratulations You Won!")
        break
    elif is_draw():
        print("Its a Draw!")
        break

    player_move('O')
    print_board()
    if is_victory('O'):
        print("Congratulations You Won!")
        break
    elif is_draw():
        print("Its a Draw!")
        break
