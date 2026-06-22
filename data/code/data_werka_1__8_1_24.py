import math

class Shape:
    def area(self):
        return 0.0

class Rectangle(Shape):
    WIDTH_MULTIPLIER = 1.0
    HEIGHT_MULTIPLIER = 1.0
    
    def __init__(self, width, height):
        self.width = width * self.WIDTH_MULTIPLIER
        self.height = height * self.HEIGHT_MULTIPLIER
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    PI = math.pi
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.PI * (self.radius ** 2)

if __name__ == '__main__':
    rect = Rectangle(5.0, 3.0)
    circle = Circle(4.0)
    
    print("Rectangle Area:", rect.area())
    print("Circle Area:", circle.area())