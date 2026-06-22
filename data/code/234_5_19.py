import itertools

class CheckerboardGenerator:
    def __init__(self, size):
        self.size = size

    def generate_checkerboard(self):
        return [[int((i + j) % 2 == 0) for j in range(self.size)] for i in range(self.size)]

if __name__ == '__main__':
    generator = CheckerboardGenerator(8)
    checkerboard = generator.generate_checkerboard()
    print(checkerboard)