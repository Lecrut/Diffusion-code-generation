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
    board_size = 5
    cb = Checkerboard(board_size)
    grid = cb.get_board()
    for row in grid:
        print(" ".join(row))