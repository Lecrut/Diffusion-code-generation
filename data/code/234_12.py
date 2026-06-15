class Checkerboard:
    def __init__(self, size):
        self.size = size
    def get_board(self):
        board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if (i + j) % 2 == 0:
                    row.append(' ')
                else:
                    row.append('X')
            board.append(row)
        return board
if __name__ == '__main__':
    board1 = Checkerboard(4)
    print("Checkerboard of size 4:")
    for row in board1.get_board():
        print(row)
    board2 = Checkerboard(3)
    print("\nCheckerboard of size 3:")
    for row in board2.get_board():
        print(row)