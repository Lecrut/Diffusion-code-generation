import math

class Shape:
    def area(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        if self.width < 0 or self.height < 0:
            raise ValueError("Width and height must be non-negative")
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius < 0:
            raise ValueError("Radius must be non-negative")
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    rect = Rectangle(6.0, 4.0)
    circle = Circle(3.0)
    
    print("Rectangle Area:", rect.area())
    print("Circle Area:", circle.area())