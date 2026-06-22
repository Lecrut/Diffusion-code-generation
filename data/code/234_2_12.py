class Checkerboard:
    def __init__(self, n):
        self.n = n
        self.board = [[0 if (i + j) % 2 == 0 else 1 for j in range(n)] for i in range(n)]

    def render(self):
        return self.board

if __name__ == '__main__':
    cb = Checkerboard(8)
    print(cb.render())