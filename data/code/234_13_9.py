class Checkerboard:
    def __init__(self, size):
        self.size = size
        self.matrix = [[(i + j) % 2 for i in range(size)] for j in range(size)]

    def get_matrix(self):
        return self.matrix

if __name__ == '__main__':
    cb = Checkerboard(10)
    print(cb.get_matrix())