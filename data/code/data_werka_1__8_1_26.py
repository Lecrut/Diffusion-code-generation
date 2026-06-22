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
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    rect_width = 6.0
    rect_height = 3.5
    circle_radius = 5.5

    rectangle = Rectangle(rect_width, rect_height)
    circle = Circle(circle_radius)

    print("Rectangle Area:", rectangle.area())
    print("Circle Area:", circle.area())