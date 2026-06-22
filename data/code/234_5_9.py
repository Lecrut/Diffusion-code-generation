import itertools

class CheckerboardGenerator:
    def __init__(self, size):
        self.size = size
        self.checkerboard = self.create_checkerboard()

    def create_checkerboard(self):
        return [[int((i + j) % 2 == 0) for j in range(self.size)] for i in range(self.size)]

if __name__ == '__main__':
    checkerboard_gen = CheckerboardGenerator(8)
    print(checkerboard_gen.checkerboard)