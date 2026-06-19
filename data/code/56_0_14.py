import math

class ShapeCalculator:
    def __init__(self, radius, side):
        self.radius = radius
        self.side = side

    def calculate_circle_area(self):
        return math.pi * self.radius ** 2

    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_square_area(self):
        return self.side ** 2

    def calculate_square_perimeter(self):
        return 4 * self.side

if __name__ == '__main__':
    circle_radius = 7.0
    square_side_length = 6.0
    calculator = ShapeCalculator(circle_radius, square_side_length)
    
    circle_area = calculator.calculate_circle_area()
    circle_perimeter = calculator.calculate_circle_perimeter()
    square_area = calculator.calculate_square_area()
    square_perimeter = calculator.calculate_square_perimeter()

    print(f"Circle Area: {circle_area}")
    print(f"Circle Perimeter (Circumference): {circle_perimeter}")
    print(f"Square Area: {square_area}")
    print(f"Square Perimeter: {square_perimeter}")