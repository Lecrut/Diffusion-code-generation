import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        RADIUS_VALUE = 5.0
        circle = Circle(RADIUS_VALUE)
        print(circle.area())
    except ValueError as e:
        print(e)