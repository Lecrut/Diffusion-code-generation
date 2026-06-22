class TriangleAreaCalculator:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        calculator = TriangleAreaCalculator(4, 8)
        area = calculator.calculate_area()
        print(area)
    except ValueError as e:
        print(e)