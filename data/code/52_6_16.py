import math

class GeometricShape:
    def area(self):
        raise Exception("This method should be overridden by subclasses")

class Square(GeometricShape):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2

class Circle(GeometricShape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    square_side = 5
    circle_radius = 7
    square = Square(square_side)
    circle = Circle(circle_radius)
    print("Square Area:", square.area())
    print("Circle Area:", circle.area())