import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    RADIUS_SAMPLE_1 = 3.0
    RADIUS_SAMPLE_2 = 8.5

    circle1 = Circle(RADIUS_SAMPLE_1)
    print(circle1.area())

    circle2 = Circle(RADIUS_SAMPLE_2)
    print(circle2.area())