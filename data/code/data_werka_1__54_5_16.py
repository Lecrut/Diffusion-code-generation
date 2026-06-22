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
    print("Area of circle with radius 5:", circle1.area())
    print("Circumference of circle with radius 5:", circle1.circumference())

    circle2 = Circle(7.5)
    print("Area of circle with radius 7.5:", circle2.area())
    print("Circumference of circle with radius 7.5:", circle2.circumference())