class CheckerboardGenerator:
    def __init__(self, size):
        self.size = size

    def generate(self):
        return [[(i + j) % 2 for j in range(self.size)] for i in range(self.size)]

if __name__ == '__main__':
    generator8x8 = CheckerboardGenerator(8)
    print("Checkerboard for n=8:")
    for row in generator8x8.generate():
        print(row)

    generator10x10 = CheckerboardGenerator(10)
    print("\nCheckerboard for n=10:")
    for row in generator10x10.generate():
        print(row)