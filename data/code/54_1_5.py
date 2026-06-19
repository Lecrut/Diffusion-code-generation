import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    sample_radius = 5.0
    circle = Circle(sample_radius)
    print(circle.area())