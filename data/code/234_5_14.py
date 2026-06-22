import itertools

class Checkerboard:
    def __init__(self, size):
        self.size = size
        self.matrix = [[(i + j) % 2 for j in range(size)] for i in range(size)]

    def get_matrix(self):
        return self.matrix

if __name__ == '__main__':
    checkerboard_instance = Checkerboard(8)
    print(checkerboard_instance.get_matrix())