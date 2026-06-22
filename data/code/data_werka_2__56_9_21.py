import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    circle_radius = 7
    rectangle_length = 8
    rectangle_width = 3

    circle = Circle(circle_radius)
    rectangle = Rectangle(rectangle_length, rectangle_width)

    circle_area = circle.calculate_area()
    circle_perimeter = circle.calculate_perimeter()

    rectangle_area = rectangle.calculate_area()
    rectangle_perimeter = rectangle.calculate_perimeter()

    print(f"Circle Area: {circle_area}")
    print(f"Circle Perimeter: {circle_perimeter}")
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Rectangle Perimeter: {rectangle_perimeter}")