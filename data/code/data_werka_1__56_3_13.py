import math

class ShapeAreaCalculator:
    def __init__(self, length, width, radius):
        self.length = length
        self.width = width
        self.radius = radius

    def calculate_rectangle_area(self):
        return self.length * self.width

    def calculate_circle_area(self):
        return math.pi * self.radius ** 2

    def compare_areas(self):
        rectangle_area = self.calculate_rectangle_area()
        circle_area = self.calculate_circle_area()
        print(f"Rectangle Area: {rectangle_area:.2f}")
        print(f"Circle Area: {circle_area:.2f}")

if __name__ == '__main__':
    length = 8.0
    width = 4.5
    radius = 6.0

    calculator = ShapeAreaCalculator(length, width, radius)
    calculator.compare_areas()