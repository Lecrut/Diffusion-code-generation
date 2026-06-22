class TriangleCalculator:
    BASE = 6
    HEIGHT = 8

    def __init__(self):
        self.base = self.BASE
        self.height = self.HEIGHT

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def get_dimensions(self):
        return f"Base: {self.base}, Height: {self.height}"

if __name__ == '__main__':
    calculator = TriangleCalculator()
    print(calculator.get_dimensions())
    print("Area:", calculator.calculate_area())