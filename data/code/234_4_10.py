class Checkerboard:
    def __init__(self, n):
        self.n = n

    @staticmethod
    def _create_row(n, i):
        return [(i + j) % 2 for j in range(n)]

    def generate_board(self):
        return [self._create_row(self.n, i) for i in range(self.n)]

if __name__ == '__main__':
    cb = Checkerboard(4)
    print(cb.generate_board())