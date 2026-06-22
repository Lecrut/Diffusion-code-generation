class SquareGrid:
    def __init__(self, size):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]

    def set_value(self, row, col, value):
        if 0 <= row < self.size and 0 <= col < self.size:
            self.grid[row][col] = value

    def get_value(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.grid[row][col]
        return None

if __name__ == '__main__':
    sample_size = 5
    grid = SquareGrid(sample_size)
    grid.set_value(2, 3, 42)
    print(f"Value at (2, 3): {grid.get_value(2, 3)}")