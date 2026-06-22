import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    try:
        r = 5.0
        c = Circle(r)
        print(f"Perimeter: {c.perimeter()}")
    except ValueError as e:
        print(e)