class Checkerboard:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
    def set_value(self, row, col, value):
        if 0 <= row < self.n and 0 <= col < self.n:
            self.board[row][col] = value
        else:
            raise IndexError("Row or column index out of bounds")
    def get_value(self, row, col):
        if 0 <= row < self.n and 0 <= col < self.n:
            return self.board[row][col]
        else:
            raise IndexError("Row or column index out of bounds")
    def display(self):
        for row in self.board:
            print(row)
if __name__ == '__main__':
    size = 4
    cb = Checkerboard(size)
    for i in range(size):
        for j in range(size):
            cb.set_value(i, j, i + j)
    print("Checkerboard:")
    cb.display()
    print("\nAccessing individual cell values:")
    print(f"Value at (0, 0): {cb.get_value(0, 0)}")
    print(f"Value at (1, 2): {cb.get_value(1, 2)}")
    print(f"Value at (3, 3): {cb.get_value(3, 3)}")