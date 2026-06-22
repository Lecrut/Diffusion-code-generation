import math

class Circle:
    def __init__(self, radius):
        if not isinstance(radius, (int, float)) or radius < 0:
            raise ValueError("Radius must be a non-negative number")
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    try:
        circle = Circle(radius=3.5)
        print(circle.perimeter())
    except ValueError as e:
        print(e)