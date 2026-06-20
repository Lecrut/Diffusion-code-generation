import math

PI = math.pi

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
        return PI * self.radius * self.radius

if __name__ == '__main__':
    sample_rect = Rectangle(8, 12)
    sample_circle = Circle(5)
    print(sample_rect.area())
    print(sample_circle.area())