import math

class CircleGeometry:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def diameter(self):
        return 2 * self.radius

if __name__ == '__main__':
    circle_geometry = CircleGeometry(5.0)
    print("Area of the circle:", circle_geometry.area())
    print("Diameter of the circle:", circle_geometry.diameter())