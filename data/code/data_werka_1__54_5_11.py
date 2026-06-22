import math

class Circle:
    PI = math.pi

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * (self.radius ** 2)

    def circumference(self):
        return 2 * self.PI * self.radius

if __name__ == '__main__':
    sample_radius = 5
    circle = Circle(sample_radius)
    print("Area:", circle.area())
    print("Circumference:", circle.circumference())