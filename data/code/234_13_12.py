class Checkerboard:
    def __init__(self, size):
        self.size = size
        self.board = [[(i + j) % 2 for j in range(size)] for i in range(size)]

    def get_board(self):
        return self.board

if __name__ == '__main__':
    cb = Checkerboard(10)
    print(cb.get_board())