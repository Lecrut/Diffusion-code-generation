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
    my_rect = Rectangle(12, 8)
    my_circle = Circle(5)
    print(my_rect.area())
    print(my_circle.area())