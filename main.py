board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def print_board():
    for x in board:
        row = ""
        for y in x:
            row += f"{y} "
        print(row)


def get_pos(num):
    num -= 1
    for i in range(3):
        for j in range(3):
            if num == 0:
                return i, j
            num -= 1


def is_available(pos, player):
    row = pos[0]
    col = pos[1]
    if board[row][col] == '-':
        board[row][col] = player
        return True


def has_won(player):
    # check rows
    for row in range(3):
        winnig = True
        for col in range(3):
            if board[row][col] != player:
                winnig = False
        if winnig:
            return True

    # check columns
    for col in range(3):
        winnig = True
        for row in range(3):
            if board[row][col] != player:
                winnig = False
        if winnig:
            return True

    # check diagonal
    winnig = True
    for step in range(3):
        if board[step][step] != player:
            winnig = False
    if winnig:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True


players = ['X', 'O']
game_on = True
move = 1
print_board()
while game_on:
    player = players[0]
    user_input = input(f"Player {player} number 1-9: ")

    if move < 9:
        if user_input.isnumeric():
            number = int(user_input)
            if 0 < number < 10:
                pos = get_pos(number)
                # print("Checking if it is taken")
                if is_available(pos, player):
                    print_board()
                    # print("Checking if won")
                    if has_won(player):
                        print(f"Player {player} won !!")
                        game_on = False
                    players.reverse()
                    move += 1
                else:
                    print("This position is taken")
            else:
                print('Number must be between 1-9')
        else:
            print('Sorry, input must be a number')
    else:
        print_board()
        print("Its a draw")
        game_on = False
