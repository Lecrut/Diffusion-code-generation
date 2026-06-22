class Checkerboard:
    def __init__(self, size):
        self.size = size
        self.board = [[0] * size for _ in range(size)]

    def render(self):
        return self.board

if __name__ == '__main__':
    board_size = 5
    cb = Checkerboard(board_size)
    print(cb.render())