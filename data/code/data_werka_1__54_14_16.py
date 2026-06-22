import math

class Circle:
    def __init__(self, radius):
        if not self._is_valid_radius(radius):
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    @staticmethod
    def _is_valid_radius(radius):
        return radius >= 0

    def area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    try:
        circle = Circle(10.0)
        print(circle.area())
    except ValueError as e:
        print(e)