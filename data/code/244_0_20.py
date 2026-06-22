import math

class AreaCalculator:
    def __init__(self, circle_radius=5, square_side_length=4):
        self.circle_radius = circle_radius
        self.square_side_length = square_side_length

    def calculate_circle_area(self):
        return math.pi * (self.circle_radius ** 2)

    def calculate_square_area(self):
        return self.square_side_length ** 2

    def total_area(self):
        return self.calculate_circle_area() + self.calculate_square_area()

if __name__ == '__main__':
    calculator = AreaCalculator()
    print("Circle area:", calculator.calculate_circle_area())
    print("Square area:", calculator.calculate_square_area())
    print("Total area:", calculator.total_area())