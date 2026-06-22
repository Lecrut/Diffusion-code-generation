import math

class Circle:
    def __init__(self, radius):
        self.set_radius(radius)

    def set_radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius

    def area(self):
        return math.pi * self._radius ** 2

    def diameter(self):
        return 2 * self._radius

if __name__ == '__main__':
    sample_radius = 3.5
    circle = Circle(sample_radius)
    print("Area:", circle.area())
    print("Diameter:", circle.diameter())