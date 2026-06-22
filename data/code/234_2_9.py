class Checkerboard:
    def __init__(self, size):
        self.size = size

    def render(self):
        return [[(i + j) % 2 for j in range(self.size)] for i in range(self.size)]

if __name__ == '__main__':
    cb = Checkerboard(8)
    print(cb.render())