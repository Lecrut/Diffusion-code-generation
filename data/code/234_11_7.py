class Checkerboard:
    def __init__(self, size):
        self.size = size
        self.board = self.generate_board()

    def generate_board(self):
        return [[(i + j) % 2 for j in range(self.size)] for i in range(self.size)]

    def get_board(self):
        return self.board

if __name__ == '__main__':
    cb3x3 = Checkerboard(3)
    print("Checkerboard for n=3:")
    for row in cb3x3.get_board():
        print(row)

    cb4x4 = Checkerboard(4)
    print("\nCheckerboard for n=4:")
    for row in cb4x4.get_board():
        print(row)