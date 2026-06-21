class TriangleAreaCalculator:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.validate_input()

    def validate_input(self):
        if not isinstance(self.base, (int, float)) or not isinstance(self.height, (int, float)):
            raise TypeError("Base and height must be numbers.")
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers.")

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        calculator = TriangleAreaCalculator(10, 5)
        area = calculator.calculate_area()
        print(area)
    except (TypeError, ValueError) as e:
        print(e)