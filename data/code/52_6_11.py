import math

class GeometricShape:
    def area(self):
        raise ValueError("Subclasses must implement this method")

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
    square = Square(side_length=5)
    print("Area of the square:", square.area())
    
    circle = Circle(radius=7)
    print("Area of the circle:", circle.area())