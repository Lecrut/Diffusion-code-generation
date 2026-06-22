import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle1 = Circle(5)
    print(circle1.area())
    print(circle1.circumference())

    circle2 = Circle(7.5)
    print(circle2.area())
    print(circle2.circumference())