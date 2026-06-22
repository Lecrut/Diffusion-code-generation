class Checkerboard:
    def __init__(self, n):
        self.n = n

    def generate_board(self):
        return [i % 2 for i in range(self.n * self.n)]

if __name__ == '__main__':
    cb1 = Checkerboard(3)
    print(cb1.generate_board())
    cb2 = Checkerboard(4)
    print(cb2.generate_board())