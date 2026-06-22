import math

class ShapeCalculator:
    def __init__(self, radius, side):
        self.radius = radius
        self.side = side

    @staticmethod
    def validate_positive(value, name):
        if value <= 0:
            raise ValueError(f"{name} must be a positive number")

    def calculate_circle_area(self):
        ShapeCalculator.validate_positive(self.radius, "Radius")
        return math.pi * self.radius ** 2

    def calculate_circle_perimeter(self):
        ShapeCalculator.validate_positive(self.radius, "Radius")
        return 2 * math.pi * self.radius

    def calculate_square_area(self):
        ShapeCalculator.validate_positive(self.side, "Side length")
        return self.side ** 2

    def calculate_square_perimeter(self):
        ShapeCalculator.validate_positive(self.side, "Side length")
        return 4 * self.side

if __name__ == '__main__':
    try:
        calculator = ShapeCalculator(radius=5.0, side=4.0)
        print(f"Circle Area: {calculator.calculate_circle_area()}")
        print(f"Circle Perimeter: {calculator.calculate_circle_perimeter()}")
        print(f"Square Area: {calculator.calculate_square_area()}")
        print(f"Square Perimeter: {calculator.calculate_square_perimeter()}")
    except ValueError as e:
        print(e)