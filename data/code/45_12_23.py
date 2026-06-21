import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0:
            raise ValueError("Radius cannot be negative")

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        circle1 = Circle(5.0)
        print(f"Area of circle 1: {circle1.area()}")
        
        circle2 = Circle(10.5)
        print(f"Area of circle 2: {circle2.area()}")
        
        invalid_circle = Circle(-3)
    except ValueError as e:
        print(e)