import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_radii = [4, 9, -1]
    for radius in sample_radii:
        try:
            circle = Circle(radius)
            print(f"Circle with radius {radius}:")
            print(f"Area: {circle.area():.2f}")
            print(f"Circumference: {circle.circumference():.2f}\n")
        except ValueError as e:
            print(e)