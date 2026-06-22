import math

class Shapes:
    def __init__(self, radius=0.0, side_length=0.0):
        self.radius = radius
        self.side_length = side_length
    
    def circle_area(self):
        if self.radius <= 0:
            raise ValueError("Radius must be positive")
        return math.pi * (self.radius ** 2)
    
    def circle_perimeter(self):
        if self.radius <= 0:
            raise ValueError("Radius must be positive")
        return 2 * math.pi * self.radius
    
    def square_area(self):
        if self.side_length <= 0:
            raise ValueError("Side length must be positive")
        return self.side_length ** 2
    
    def square_perimeter(self):
        if self.side_length <= 0:
            raise ValueError("Side length must be positive")
        return 4 * self.side_length

if __name__ == '__main__':
    circle_radius = 5.0
    square_side_length = 10.0
    
    shape = Shapes(radius=circle_radius, side_length=square_side_length)
    
    print(f"Circle Area: {shape.circle_area()}")
    print(f"Circle Perimeter: {shape.circle_perimeter()}")
    print(f"Square Area: {shape.square_area()}")
    print(f"Square Perimeter: {shape.square_perimeter()}")