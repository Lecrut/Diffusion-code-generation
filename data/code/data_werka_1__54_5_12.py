import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_radius = 5.0
    circle_instance = Circle(sample_radius)
    print("Area:", circle_instance.area())
    print("Circumference:", circle_instance.circumference())