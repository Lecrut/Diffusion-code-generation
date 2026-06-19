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
    shape_data = {
        'circle_radius': 5.0,
        'square_side': 4.0
    }
    
    calculator = ShapeCalculator(shape_data['circle_radius'], shape_data['square_side'])
    
    circle_area = calculator.calculate_circle_area()
    circle_perimeter = calculator.calculate_circle_perimeter()
    square_area = calculator.calculate_square_area()
    square_perimeter = calculator.calculate_square_perimeter()
    
    print(f"Circle Area: {circle_area}")
    print(f"Circle Perimeter: {circle_perimeter}")
    print(f"Square Area: {square_area}")
    print(f"Square Perimeter: {square_perimeter}")