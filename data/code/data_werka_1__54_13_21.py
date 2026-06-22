import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def diameter(self):
        return 2 * self.radius

if __name__ == '__main__':
    sample_radius = 3.5
    circle = Circle(sample_radius)
    print("Area:", circle.area())
    print("Diameter:", circle.diameter())