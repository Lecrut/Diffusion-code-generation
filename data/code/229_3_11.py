class SquareGrid:
    def __init__(self, size):
        self.size = size

    def print_grid(self):
        for _ in range(self.size):
            print('*' * self.size)

if __name__ == '__main__':
    grid_size = 8
    square_grid = SquareGrid(grid_size)
    square_grid.print_grid()