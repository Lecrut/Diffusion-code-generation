import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def get_diameter(self):
        return 2 * self.radius

if __name__ == '__main__':
    circle = Circle(5)
    area = circle.calculate_area()
    diameter = circle.get_diameter()
    print(f"Area: {area}")
    print(f"Diameter: {diameter}")