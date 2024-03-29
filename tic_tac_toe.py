# Board setup

blank = "-"
player_1 = "X"
player_2 = "O"


class Board:
    def __init__(self):
        self.board_state = [[blank, blank, blank],
                            [blank, blank, blank],
                            [blank, blank, blank]]

    def get_board(self):
        return self.board_state

    def get_board_str(self):
        return (f"""
{self.get_square(0, 0)} {self.get_square(1, 0)} {self.get_square(2, 0)}
{self.get_square(0, 1)} {self.get_square(1, 1)} {self.get_square(2, 1)}
{self.get_square(0, 2)} {self.get_square(1, 2)} {self.get_square(2, 2)}
""")

    def set_square(self, x, y, status):
        self.board_state[x][y] = status

    def get_square(self, x, y):
        return self.board_state[x][y]

    def get_winner(self):
        for i in range(3):
            if (self.get_square(i, 0) == self.get_square(i, 1) == self.get_square(i, 2)) and self.get_square(i,
                                                                                                             0) != blank:
                return self.get_square(i, 0)
            if (self.get_square(0, i) == self.get_square(1, i) == self.get_square(2, i)) and self.get_square(0,
                                                                                                             i) != blank:
                return self.get_square(0, i)
        if (self.get_square(0, 0) == self.get_square(1, 1) == self.get_square(2, 2)) and self.get_square(0, 0) != blank:
            return self.get_square(0, 0)
        elif (self.get_square(2, 0) == self.get_square(1, 1) == self.get_square(0, 2)) and self.get_square(2,
                                                                                                           0) != blank:
            return self.get_square(2, 0)

    def fill_board(self, winner):
        if winner != blank:
            for i in range(3):
                for j in range(3):
                    self.set_square(i, j, winner)


class UltimateBoard:
    def __init__(self):
        self.board_state = [[Board(), Board(), Board()],
                            [Board(), Board(), Board()],
                            [Board(), Board(), Board()]]

        self.status_board = Board()

    def get_mini_board(self, a, b):
        return self.board_state[a][b]

    def get_square(self, a, b, x, y):
        return self.get_mini_board(a, b).get_square(x, y)

    def set_square(self, a, b, x, y, player):
        self.board_state[a][b].set_square(x, y, player)

    def get_board_str(self):
        return (f"""
{self.get_square(0, 0, 0, 0)} {self.get_square(0, 0, 1, 0)} {self.get_square(0, 0, 2, 0)}   {self.get_square(1, 0, 0, 0)} {self.get_square(1, 0, 1, 0)} {self.get_square(1, 0, 2, 0)}   {self.get_square(2, 0, 0, 0)} {self.get_square(2, 0, 1, 0)} {self.get_square(2, 0, 2, 0)}
{self.get_square(0, 0, 0, 1)} {self.get_square(0, 0, 1, 1)} {self.get_square(0, 0, 2, 1)}   {self.get_square(1, 0, 0, 1)} {self.get_square(1, 0, 1, 1)} {self.get_square(1, 0, 2, 1)}   {self.get_square(2, 0, 0, 1)} {self.get_square(2, 0, 1, 1)} {self.get_square(2, 0, 2, 1)}
{self.get_square(0, 0, 0, 2)} {self.get_square(0, 0, 1, 2)} {self.get_square(0, 0, 2, 2)}   {self.get_square(1, 0, 0, 2)} {self.get_square(1, 0, 1, 2)} {self.get_square(1, 0, 2, 2)}   {self.get_square(2, 0, 0, 2)} {self.get_square(2, 0, 1, 2)} {self.get_square(2, 0, 2, 2)}

{self.get_square(0, 1, 0, 0)} {self.get_square(0, 1, 1, 0)} {self.get_square(0, 1, 2, 0)}   {self.get_square(1, 1, 0, 0)} {self.get_square(1, 1, 1, 0)} {self.get_square(1, 1, 2, 0)}   {self.get_square(2, 1, 0, 0)} {self.get_square(2, 1, 1, 0)} {self.get_square(2, 1, 2, 0)}
{self.get_square(0, 1, 0, 1)} {self.get_square(0, 1, 1, 1)} {self.get_square(0, 1, 2, 1)}   {self.get_square(1, 1, 0, 1)} {self.get_square(1, 1, 1, 1)} {self.get_square(1, 1, 2, 1)}   {self.get_square(2, 1, 0, 1)} {self.get_square(2, 1, 1, 1)} {self.get_square(2, 1, 2, 1)}
{self.get_square(0, 1, 0, 2)} {self.get_square(0, 1, 1, 2)} {self.get_square(0, 1, 2, 2)}   {self.get_square(1, 1, 0, 2)} {self.get_square(1, 1, 1, 2)} {self.get_square(1, 1, 2, 2)}   {self.get_square(2, 1, 0, 2)} {self.get_square(2, 1, 1, 2)} {self.get_square(2, 1, 2, 2)}

{self.get_square(0, 2, 0, 0)} {self.get_square(0, 2, 1, 0)} {self.get_square(0, 2, 2, 0)}   {self.get_square(1, 2, 0, 0)} {self.get_square(1, 2, 1, 0)} {self.get_square(1, 2, 2, 0)}   {self.get_square(2, 2, 0, 0)} {self.get_square(2, 2, 1, 0)} {self.get_square(2, 2, 2, 0)}
{self.get_square(0, 2, 0, 1)} {self.get_square(0, 2, 1, 1)} {self.get_square(0, 2, 2, 1)}   {self.get_square(1, 2, 0, 1)} {self.get_square(1, 2, 1, 1)} {self.get_square(1, 2, 2, 1)}   {self.get_square(2, 2, 0, 1)} {self.get_square(2, 2, 1, 1)} {self.get_square(2, 2, 2, 1)}
{self.get_square(0, 2, 0, 2)} {self.get_square(0, 2, 1, 2)} {self.get_square(0, 2, 2, 2)}   {self.get_square(1, 2, 0, 2)} {self.get_square(1, 2, 1, 2)} {self.get_square(1, 2, 2, 2)}   {self.get_square(2, 2, 0, 2)} {self.get_square(2, 2, 1, 2)} {self.get_square(2, 2, 2, 2)}
""")

    def fill_boards(self):
        for i in range(3):
            for j in range(3):
                if self.get_mini_board(i, j).get_winner() is not None:
                    self.get_mini_board(i, j).fill_board(self.get_mini_board(i, j).get_winner())
                    self.status_board.set_square(i, j, self.get_mini_board(i, j).get_winner())

    def check_status_win(self):
        if self.status_board.get_winner() is not None:
            return self.status_board.get_winner()


class Players:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.current_player = self.player_1

    def get_player(self):
        return self.current_player

    def change_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        elif self.current_player == self.player_2:
            self.current_player = self.player_1


def play_regular():
    board = Board()
    print(board.get_board_str())
    players = Players(player_1, player_2)
    while True:
        try:
            move = input(f"{players.get_player()}: ")
            if move.lower() == "quit":
                break
            move_x = eval(move[0])
            move_y = eval(move[1])
            if board.get_square(move_x - 1, move_y - 1) == blank:
                board.set_square(move_x - 1, move_y - 1, players.get_player())
                players.change_player()
                print(board.get_board_str())
            else:
                print("This space is already taken!")
        except:
            print("Invalid entry")

        if board.get_winner() is not None:
            board.fill_board(board.get_winner())
            print(board.get_board_str())
            print(f"THE WINNER IS {board.get_winner()}!")
            break


def play_ultimate():
    board = UltimateBoard()
    print(board.get_board_str())
    players = Players(player_1, player_2)
    while True:
        try:
            move = input(f"{players.get_player()}: ")
            if len(move) > 4:
                raise Exception
            if move.lower() == "quit":
                break
            move_a = eval(move[0]) - 1
            move_b = eval(move[1]) - 1
            move_x = eval(move[2]) - 1
            move_y = eval(move[3]) - 1

            if board.get_square(move_a, move_b, move_x, move_y) == blank:
                board.set_square(move_a, move_b, move_x, move_y, players.get_player())
                board.fill_boards()
                players.change_player()
                print(board.get_board_str())
            else:
                print("This space is already taken!")
        except:
            print("Invalid Input")

        if board.check_status_win() is not None:
            for i in range(3):
                for j in range(3):
                    board.get_mini_board(i, j).fill_board(board.check_status_win())
            print(board.get_board_str())
            print(f"THE WINNER IS {board.check_status_win()}!")
            break


def main():
    print("""Welcome to Tic Tac Toe!
Type 'REGULAR' to play the traditional game or 'ULTIMATE' to play on a 3x3 grid of 3x3 grids!
To exit the game, type 'QUIT' anytime.""")
    while True:
        game_type = input("Which game would you like to play? (REGULAR/ULTIMATE): ")
        if game_type.lower() == "quit":
            break
        if game_type.lower() == "regular":
            print("""\nTo enter a move, type the coordinates of the square you want to place your piece in.
For example, to place your piece in the top left corner, type '11'.""")
            play_regular()
        elif game_type.lower() == "ultimate":
            print("""\nTo enter a move, type the coordinates of the grid you want to place in, followed by the coordinates of the square inside of that grid.
For example, to place your piece in the center of the top left grid, type '1122'.""")
            play_ultimate()
        else:
            print("Invalid Input")


if __name__ == '__main__':
    main()