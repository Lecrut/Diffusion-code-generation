import math

class Shape:
    def area(self):
        raise Exception("This method should be overridden by subclasses")

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
    
    print("Area of the square:", square.area())
    print("Area of the circle:", circle.area())