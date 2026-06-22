class Checkerboard:
    def __init__(self, size=10):
        self.size = size
        self.matrix = [[(i + j) % 2 for i in range(self.size)] for j in range(self.size)]

    def print_board(self):
        for row in self.matrix:
            print(" ".join("#" if cell else " " for cell in row))

if __name__ == '__main__':
    cb = Checkerboard(4)
    print("Checkerboard for size 4:")
    cb.print_board()
    print("\nCheckerboard for size 5:")
    cb = Checkerboard(5)
    cb.print_board()