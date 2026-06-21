import math

class Shape:
    def calculate_area(self):
        raise ValueError("Unsupported shape type")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

if __name__ == '__main__':
    circle = Circle(radius=5.0)
    rectangle = Rectangle(width=4.0, height=6.0)

    print("Circle Area:", circle.calculate_area())
    print("Rectangle Area:", rectangle.calculate_area())