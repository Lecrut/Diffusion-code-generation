import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    sample_circle1 = Circle(4)
    print(f"Area of circle with radius {sample_circle1.radius}: {sample_circle1.area()}")

    sample_circle2 = Circle(7.5)
    print(f"Area of circle with radius {sample_circle2.radius}: {sample_circle2.area()}")