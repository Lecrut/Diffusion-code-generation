class SquareGrid:
    def __init__(self, side):
        self.side = side
        self.grid = [[0] * side for _ in range(side)]

    def set_cell(self, row, col, value):
        if 0 <= row < self.side and 0 <= col < self.side:
            self.grid[row][col] = value

    def get_cell(self, row, col):
        if 0 <= row < self.side and 0 <= col < self.side:
            return self.grid[row][col]
        return None

if __name__ == '__main__':
    grid_size = 5
    my_grid = SquareGrid(grid_size)
    my_grid.set_cell(2, 3, 42)
    print("Cell value at (2, 3):", my_grid.get_cell(2, 3))