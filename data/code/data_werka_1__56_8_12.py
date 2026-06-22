import math

class ShapeCalculator:
    def __init__(self, circle_radius, square_side):
        self.circle_radius = circle_radius
        self.square_side = square_side

    def calculate_circumference(self):
        return 2 * math.pi * self.circle_radius

    def calculate_perimeter(self):
        return 4 * self.square_side

if __name__ == '__main__':
    calculator = ShapeCalculator(circle_radius=3.0, square_side=6.0)
    print("Circumference of the circle:", calculator.calculate_circumference())
    print("Perimeter of the square:", calculator.calculate_perimeter())