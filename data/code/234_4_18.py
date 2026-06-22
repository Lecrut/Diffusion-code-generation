class CheckerboardGenerator:
    def __init__(self, dimension):
        self.dimension = dimension

    def generate_checkerboard(self):
        return [i % 2 ^ j % 2 for i in range(self.dimension) for j in range(self.dimension)]

if __name__ == '__main__':
    generator1 = CheckerboardGenerator(3)
    print(f"n=3:\n{generator1.generate_checkerboard()}")

    generator2 = CheckerboardGenerator(4)
    print(f"n=4:\n{generator2.generate_checkerboard()}")