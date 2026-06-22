class TriangleAreaCalculator:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle = TriangleAreaCalculator(10, 5)
    print(triangle.calculate())