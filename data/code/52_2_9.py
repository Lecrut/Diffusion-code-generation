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
    sample_radii = [5, 10, -3]
    for radius in sample_radii:
        try:
            circle = Circle(radius)
            print(f"The area of the circle with radius {radius} is {circle.area():.2f}")
            print(f"The circumference of the circle with radius {radius} is {circle.circumference():.2f}")
        except ValueError as e:
            print(e)