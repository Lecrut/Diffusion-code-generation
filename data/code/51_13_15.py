import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    hard_coded_radius = 4.5
    try:
        circle = Circle(hard_coded_radius)
        print(circle.perimeter())
    except ValueError as e:
        print(e)