class Checkerboard:
    def __init__(self, size):
        self.size = size
        self.matrix = [[(i + j) % 2 for j in range(size)] for i in range(size)]

if __name__ == '__main__':
    cb = Checkerboard(10)
    print(cb.matrix)