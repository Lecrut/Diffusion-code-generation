class SquareGrid:

    def __init__(self, size):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def set_cell(self, row, col, value):
        if 0 <= row < self.size and 0 <= col < self.size:
            self.grid[row][col] = value

    def get_cell(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.grid[row][col]
        return None
if __name__ == '__main__':
    grid = SquareGrid(3)
    grid.set_cell(1, 1, 5)
    print(grid.get_cell(1, 1))