import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle = Circle(3.14)
    print(circle.circumference())