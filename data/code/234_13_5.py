class Checkerboard:
    def __init__(self, size):
        self.size = size

    def generate_board(self):
        return [[(i + j) % 2 for i in range(self.size)] for j in range(self.size)]

if __name__ == '__main__':
    cb = Checkerboard(10)
    board = cb.generate_board()
    print(board)