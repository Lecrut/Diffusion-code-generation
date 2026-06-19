import math

class ShapeCalculator:
    def __init__(self, radius=None, side=None):
        if radius is not None and radius <= 0:
            raise ValueError("Radius must be positive")
        if side is not None and side <= 0:
            raise ValueError("Side length must be positive")
        self.radius = radius
        self.side = side

    def calculate_circle_area(self):
        if self.radius is None:
            raise ValueError("Radius not set for circle calculation")
        return math.pi * (self.radius ** 2)

    def calculate_circle_perimeter(self):
        if self.radius is None:
            raise ValueError("Radius not set for circle calculation")
        return 2 * math.pi * self.radius

    def calculate_square_area(self):
        if self.side is None:
            raise ValueError("Side length not set for square calculation")
        return self.side ** 2

    def calculate_square_perimeter(self):
        if self.side is None:
            raise ValueError("Side length not set for square calculation")
        return 4 * self.side

if __name__ == '__main__':
    try:
        calculator = ShapeCalculator(radius=5.0, side=4.0)
        print(f"Circle Area: {calculator.calculate_circle_area()}")
        print(f"Circle Perimeter (Circumference): {calculator.calculate_circle_perimeter()}")
        print(f"Square Area: {calculator.calculate_square_area()}")
        print(f"Square Perimeter: {calculator.calculate_square_perimeter()}")
    except ValueError as e:
        print(e)