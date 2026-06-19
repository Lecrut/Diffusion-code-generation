import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    def area(self):
        return calculate_circle_area(self.radius)

if __name__ == '__main__':
    sample_radii = [2.5, 15, -4]
    for radius in sample_radii:
        try:
            circle = Circle(radius)
            print(f"The area of the circle with radius {radius} is {circle.area():.2f}")
        except ValueError as e:
            print(e)