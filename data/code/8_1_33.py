import math

class Shape:
    def area(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    PI = math.pi

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * (self.radius ** 2)

if __name__ == '__main__':
    rect_width = 10.5
    rect_height = 5.0
    circle_radius = 4.0

    rectangle = Rectangle(rect_width, rect_height)
    circle = Circle(circle_radius)

    print("Rectangle Area:", rectangle.area())
    print("Circle Area:", circle.area())