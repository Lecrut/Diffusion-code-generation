import math

class Circle:
    def __init__(self, radius):
        if not self._is_valid_radius(radius):
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return self._calculate_area()

    def _calculate_area(self):
        return math.pi * (self.radius ** 2)

    @staticmethod
    def _is_valid_radius(radius):
        return radius >= 0

if __name__ == '__main__':
    try:
        circle = Circle(3)
        print("Area of circle with radius 3:", circle.area())
    except ValueError as e:
        print(e)