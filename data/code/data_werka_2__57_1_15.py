import math

class Shape:
    def calculate_area(self):
        raise ValueError("This method should be overridden by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return area

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        return area

if __name__ == '__main__':
    circle_radius = 7.0
    rectangle_width = 3.0
    rectangle_height = 9.0

    circle = Circle(radius=circle_radius)
    rectangle = Rectangle(width=rectangle_width, height=rectangle_height)

    print("Circle Area:", circle.calculate_area())
    print("Rectangle Area:", rectangle.calculate_area())