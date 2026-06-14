class Checkerboard:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
    def set_value(self, row, col, value):
        if 0 <= row < self.n and 0 <= col < self.n:
            self.board[row][col] = value
    def get_value(self, row, col):
        if 0 <= row < self.n and 0 <= col < self.n:
            return self.board[row][col]
        return None
    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()
if __name__ == '__main__':
    size = 4
    cb = Checkerboard(size)
    cb.set_value(0, 0, 1)
    cb.set_value(0, 1, 0)
    cb.set_value(1, 0, 0)
    cb.set_value(1, 1, 1)
    cb.set_value(2, 2, 0)
    cb.set_value(3, 3, 1)
    print("Checkerboard:")
    cb.display()
    print("\nAccessing individual cell values:")
    print(f"Value at (0, 0): {cb.get_value(0, 0)}")
    print(f"Value at (1, 1): {cb.get_value(1, 1)}")
    print(f"Value at (3, 3): {cb.get_value(3, 3)}")
    print(f"Value at (2, 0) (uninitialized): {cb.get_value(2, 0)}")