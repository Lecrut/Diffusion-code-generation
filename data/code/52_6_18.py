import math

class Shape:
    def area(self):
        raise ValueError("Subclasses must implement the area method")

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    square = Square(4)
    circle = Circle(3)
    
    print("Square Area:", square.area())
    print("Circle Area:", circle.area())