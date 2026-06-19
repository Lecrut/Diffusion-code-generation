import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_radius = 7.5
    circle = Circle(sample_radius)
    print(f"Area of the circle with radius {sample_radius}: {circle.area()}")
    print(f"Circumference of the circle with radius {sample_radius}: {circle.circumference()}")