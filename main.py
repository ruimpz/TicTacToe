from random import randint

class Player:
    def __init__(self,name, sym):
        self.name = name
        self.sym = sym

    def get_play(self):
        while True:
            play = input(self.name + "'s turn: ")
            if play in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return play
            else:
                print("Invalid play. Not a valid square.")


def greet():
    print("Welcome to Tic-Tac-Toe.\nFill in vertical, horizontal or diagonal lines to win.")
    print("Select the tile with the numbers [1..9]")
    draw_board([0, "1", "2", "3", "4", "5", "6", "7", "8", "9"])

def draw_board(board_state):
    print()
    print(" {} | {} | {} ".format(board_state[1], board_state[2], board_state[3]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board_state[4], board_state[5], board_state[6]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board_state[7], board_state[8], board_state[9]))
    print()


def get_sym(player, cpu):
    while True:
        sym = input("Choose you symbol: 'X' or 'O'\n")
        if sym == "X" or sym  == "x":
            player.sym = "X"
            cpu .sym = "O"
            print()
            break
        elif sym == "O" or sym == "o":
            player.sym = "O"
            cpu.sym = "X"
            print()
            break
        else:
            print("Please insert a valid symbol.\n")


def get_turn():
    if randint(0, 1) == 0:
        print("Player goes first.\n")
        return True
    else:
        print("Computer goes first.\n")
        return False


def game_action(board_state, player, cpu, turn):
    if turn:
        while True:
            play = int(player.get_play())
            if board_state[play] == " ":
                board_state[play] = player.sym
                board_state[0] += 1
                break
            else:
                print("Invalid play. That square is already filled.\n")
    else:
        while True:
            play = cpu_logic(board_state, cpu, player)
            print("Computer's turn:")
            board_state[play] = cpu.sym
            board_state[0] += 1
            break


def check_win(board_state, player, cpu):
    if (board_state[1] == player.sym and board_state[2] == player.sym and board_state[3] == player.sym) or \
        (board_state[4] == player.sym and board_state[5] == player.sym and board_state[6] == player.sym) or \
        (board_state[7] == player.sym and board_state[8] == player.sym and board_state[9] == player.sym) or \
        (board_state[1] == player.sym and board_state[4] == player.sym and board_state[7] == player.sym) or \
        (board_state[2] == player.sym and board_state[5] == player.sym and board_state[8] == player.sym) or \
        (board_state[3] == player.sym and board_state[6] == player.sym and board_state[9] == player.sym) or \
        (board_state[1] == player.sym and board_state[5] == player.sym and board_state[9] == player.sym) or \
        (board_state[3] == player.sym and board_state[5] == player.sym and board_state[7] == player.sym):
            return 0
    elif (board_state[1] == cpu.sym and board_state[2] == cpu.sym and board_state[3] == cpu.sym) or \
        (board_state[4] == cpu.sym and board_state[5] == cpu.sym and board_state[6] == cpu.sym) or \
        (board_state[7] == cpu.sym and board_state[8] == cpu.sym and board_state[9] == cpu.sym) or \
        (board_state[1] == cpu.sym and board_state[4] == cpu.sym and board_state[7] == cpu.sym) or \
        (board_state[2] == cpu.sym and board_state[5] == cpu.sym and board_state[8] == cpu.sym) or \
        (board_state[3] == cpu.sym and board_state[6] == cpu.sym and board_state[9] == cpu.sym) or \
        (board_state[1] == cpu.sym and board_state[5] == cpu.sym and board_state[9] == cpu.sym) or \
        (board_state[3] == cpu.sym and board_state[5] == cpu.sym and board_state[7] == cpu.sym):
            return 1
    elif board_state[1] != " " and board_state[2] != " " and board_state[3] != " " and \
        board_state[4] != " " and board_state[5] != " " and board_state[6] != " " and \
        board_state[7] != " " and board_state[8] != " " and board_state[9] != " " and board_state[0] != 0:
        return 2
    else:
        return None


def cpu_logic(board_state, cpu, player):
    if cpu_winning_play(board_state, cpu) != None:
        return cpu_winning_play(board_state, cpu)
    elif player_winning_play(board_state, player) != None:
        return player_winning_play(board_state, player)
    else:
        play = 0
        while board_state[play] != " ":
            play = randint(1, 9)
        return play



def cpu_winning_play(board_state, cpu):
    if (board_state[1] == cpu.sym and board_state[2] == cpu.sym and board_state[3] == " "):
        return 3
    elif (board_state[1] == cpu.sym and board_state[3] == cpu.sym and board_state[2] == " "):
        return 2
    elif (board_state[2] == cpu.sym and board_state[3] == cpu.sym and board_state[1] == " "):
        return 1
    elif (board_state[4] == cpu.sym and board_state[5] == cpu.sym and board_state[6] == " "):
        return 6
    elif (board_state[4] == cpu.sym and board_state[6] == cpu.sym and board_state[5] == " "):
        return 5
    elif (board_state[5] == cpu.sym and board_state[6] == cpu.sym and board_state[4] == " "):
        return 4
    elif (board_state[7] == cpu.sym and board_state[8] == cpu.sym and board_state[9] == " "):
        return 9
    elif (board_state[7] == cpu.sym and board_state[9] == cpu.sym and board_state[8] == " "):
        return 8
    elif (board_state[8] == cpu.sym and board_state[9] == cpu.sym and board_state[7] == " "):
        return 7
    elif (board_state[1] == cpu.sym and board_state[4] == cpu.sym and board_state[7] == " "):
        return 7
    elif (board_state[1] == cpu.sym and board_state[7] == cpu.sym and board_state[4] == " "):
        return 4
    elif (board_state[4] == cpu.sym and board_state[7] == cpu.sym and board_state[1] == " "):
        return 1
    elif (board_state[2] == cpu.sym and board_state[5] == cpu.sym and board_state[8] == " "):
        return 8
    elif (board_state[2] == cpu.sym and board_state[8] == cpu.sym and board_state[5] == " "):
        return 5
    elif (board_state[5] == cpu.sym and board_state[8] == cpu.sym and board_state[2] == " "):
        return 2
    elif (board_state[3] == cpu.sym and board_state[6] == cpu.sym and board_state[9] == " "):
        return 9
    elif (board_state[3] == cpu.sym and board_state[9] == cpu.sym and board_state[6] == " "):
        return 6
    elif (board_state[6] == cpu.sym and board_state[9] == cpu.sym and board_state[3] == " "):
        return 3
    elif (board_state[1] == cpu.sym and board_state[5] == cpu.sym and board_state[9] == " "):
        return 9
    elif (board_state[1] == cpu.sym and board_state[9] == cpu.sym and board_state[5] == " "):
        return 5
    elif (board_state[5] == cpu.sym and board_state[9] == cpu.sym and board_state[1] == " "):
        return 1
    elif (board_state[3] == cpu.sym and board_state[5] == cpu.sym and board_state[7] == " "):
        return 7
    elif (board_state[3] == cpu.sym and board_state[7] == cpu.sym and board_state[5] == " "):
        return 5
    elif (board_state[5] == cpu.sym and board_state[7] == cpu.sym and board_state[3] == " "):
        return 3
    else:
        return None


def player_winning_play(board_state, player):
    if (board_state[1] == player.sym and board_state[2] == player.sym and board_state[3] == " "):
        return 3
    elif (board_state[1] == player.sym and board_state[3] == player.sym and board_state[2] == " "):
        return 2
    elif (board_state[2] == player.sym and board_state[3] == player.sym and board_state[1] == " "):
        return 1
    elif (board_state[4] == player.sym and board_state[5] == player.sym and board_state[6] == " "):
        return 6
    elif (board_state[4] == player.sym and board_state[6] == player.sym and board_state[5] == " "):
        return 5
    elif (board_state[5] == player.sym and board_state[6] == player.sym and board_state[4] == " "):
        return 4
    elif (board_state[7] == player.sym and board_state[8] == player.sym and board_state[9] == " "):
        return 9
    elif (board_state[7] == player.sym and board_state[9] == player.sym and board_state[8] == " "):
        return 8
    elif (board_state[8] == player.sym and board_state[9] == player.sym and board_state[7] == " "):
        return 7
    elif (board_state[1] == player.sym and board_state[4] == player.sym and board_state[7] == " "):
        return 7
    elif (board_state[1] == player.sym and board_state[7] == player.sym and board_state[4] == " "):
        return 4
    elif (board_state[4] == player.sym and board_state[7] == player.sym and board_state[1] == " "):
        return 1
    elif (board_state[2] == player.sym and board_state[5] == player.sym and board_state[8] == " "):
        return 8
    elif (board_state[2] == player.sym and board_state[8] == player.sym and board_state[5] == " "):
        return 5
    elif (board_state[5] == player.sym and board_state[8] == player.sym and board_state[2] == " "):
        return 2
    elif (board_state[3] == player.sym and board_state[6] == player.sym and board_state[9] == " "):
        return 9
    elif (board_state[3] == player.sym and board_state[9] == player.sym and board_state[6] == " "):
        return 6
    elif (board_state[6] == player.sym and board_state[9] == player.sym and board_state[3] == " "):
        return 3
    elif (board_state[1] == player.sym and board_state[5] == player.sym and board_state[9] == " "):
        return 9
    elif (board_state[1] == player.sym and board_state[9] == player.sym and board_state[5] == " "):
        return 5
    elif (board_state[5] == player.sym and board_state[9] == player.sym and board_state[1] == " "):
        return 1
    elif (board_state[3] == player.sym and board_state[5] == player.sym and board_state[7] == " "):
        return 7
    elif (board_state[3] == player.sym and board_state[7] == player.sym and board_state[5] == " "):
        return 5
    elif (board_state[5] == player.sym and board_state[7] == player.sym and board_state[3] == " "):
        return 3
    else:
        return None



def main():
    greet()
    player = Player("Player", " ")
    cpu = Player("Computer", " ")
    get_sym(player, cpu)
    board_state = [0, " ", " ", " ", " ", " ", " ", " ", " ", " ",]
    turn = get_turn()

#GAMELOOP
    while check_win(board_state, player, cpu) != 0 and check_win(board_state, player, cpu) != 1 and \
            check_win(board_state, player, cpu) != 2:
        game_action(board_state, player, cpu, turn)
        turn = not turn
        draw_board(board_state)

    if check_win(board_state, player, cpu) == 0:
        print("Congratulation, you win!")
    elif check_win(board_state, player, cpu) == 1:
        print("Computer wins.")
    else:
        print("It's a tie.")


if __name__ == '__main__':
    main()
