import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0:
            raise ValueError("Radius cannot be negative")

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle_properties = {
        'radius': 5.0
    }
    try:
        circle = Circle(circle_properties['radius'])
        print("Area:", circle.area())
        print("Circumference:", circle.circumference())
    except ValueError as e:
        print(e)