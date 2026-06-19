import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    circle1 = Circle(3)
    circle2 = Circle(7.5)

    print(f"Area of circle with radius {circle1.radius}: {circle1.area()}")
    print(f"Area of circle with radius {circle2.radius}: {circle2.area()}")