import math

class ShapeCalculator:
    def __init__(self, radius=0.0, side_length=0.0):
        self.radius = radius
        self.side_length = side_length

    def calculate_circle_area(self):
        return math.pi * self.radius ** 2

    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_square_area(self):
        return self.side_length ** 2

    def calculate_square_perimeter(self):
        return 4 * self.side_length

if __name__ == '__main__':
    shape_calculator = ShapeCalculator(radius=5.0, side_length=4.0)
    
    circle_area = shape_calculator.calculate_circle_area()
    circle_perimeter = shape_calculator.calculate_circle_perimeter()
    square_area = shape_calculator.calculate_square_area()
    square_perimeter = shape_calculator.calculate_square_perimeter()

    print(f"Circle Area: {circle_area}")
    print(f"Circle Perimeter (Circumference): {circle_perimeter}")
    print(f"Square Area: {square_area}")
    print(f"Square Perimeter: {square_perimeter}")