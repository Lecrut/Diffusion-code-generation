class SquareGrid:

    def __init__(self, side_length):
        self.side_length = side_length
        self.grid = [[0 for _ in range(side_length)] for _ in range(side_length)]

    def set_cell(self, row, col, value):
        if 0 <= row < self.side_length and 0 <= col < self.side_length:
            self.grid[row][col] = value

    def get_cell(self, row, col):
        if 0 <= row < self.side_length and 0 <= col < self.side_length:
            return self.grid[row][col]
        else:
            raise IndexError('Cell indices out of bounds')
if __name__ == '__main__':
    grid_size = 3
    my_grid = SquareGrid(grid_size)
    my_grid.set_cell(0, 0, 1)
    my_grid.set_cell(1, 1, 2)
    my_grid.set_cell(2, 2, 3)
    print(my_grid.get_cell(0, 0))
    print(my_grid.get_cell(1, 1))
    print(my_grid.get_cell(2, 2))