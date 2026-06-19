import math

class Shape:
    def area(self):
        return 0.0

class Rectangle(Shape):
    WIDTH = 5.0
    HEIGHT = 3.0
    
    def __init__(self, width=None, height=None):
        self.width = width if width is not None else Rectangle.WIDTH
        self.height = height if height is not None else Rectangle.HEIGHT
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    RADIUS = 4.0
    
    def __init__(self, radius=None):
        self.radius = radius if radius is not None else Circle.RADIUS
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    rect = Rectangle()
    circle = Circle()

    print("Rectangle Area:", rect.area())
    print("Circle Area:", circle.area())