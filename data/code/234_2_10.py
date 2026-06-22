class Checkerboard:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
    
    def render(self):
        return self.board

if __name__ == '__main__':
    size = 3
    cb = Checkerboard(size)
    print(cb.render())