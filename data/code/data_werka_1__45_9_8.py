import math

PI = math.pi

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2

    def diameter(self):
        return 2 * self.radius

if __name__ == '__main__':
    sample_radius = 10.0
    circle = Circle(sample_radius)
    print("Area:", circle.area())
    print("Diameter:", circle.diameter())