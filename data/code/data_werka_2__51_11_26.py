import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        if not isinstance(self.radius, (int, float)) or self.radius < 0:
            raise ValueError("Radius must be a non-negative number")
    
    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    try:
        circle = Circle(radius=15)
        print(circle.perimeter())
    except ValueError as e:
        print(e)