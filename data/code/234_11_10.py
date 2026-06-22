class Checkerboard:
    def __init__(self, size):
        self.size = size
        self.board = [[(i + j) % 2 for j in range(size)] for i in range(size)]

    def print_board(self):
        for row in self.board:
            print(row)

if __name__ == '__main__':
    cb3x3 = Checkerboard(3)
    print("Checkerboard for n=3:")
    cb3x3.print_board()

    cb4x4 = Checkerboard(4)
    print("\nCheckerboard for n=4:")
    cb4x4.print_board()