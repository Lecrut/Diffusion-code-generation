class Checkerboard:
    def __init__(self, size):
        self.size = size
    def get_grid(self):
        grid = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if (i + j) % 2 == 0:
                    row.append(1)
                else:
                    row.append(0)
            grid.append(row)
        return grid
if __name__ == '__main__':
    board_size = 4
    cb = Checkerboard(board_size)
    board = cb.get_grid()
    for row in board:
        print(row)