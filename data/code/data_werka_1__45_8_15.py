import math

class Circle:
    def __init__(self, radius):
        self._validate_radius(radius)
        self.radius = radius

    def _validate_radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius < 0:
            raise ValueError("Radius cannot be negative")

    def area(self):
        return self._calculate_area()

    def _calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        circle = Circle(3)
        print(f"Area of circle with radius 3: {circle.area()}")
    except Exception as e:
        print(e)