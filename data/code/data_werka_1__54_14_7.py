import math

class Circle:
    def __init__(self, radius):
        self._validate_radius(radius)
        self.radius = radius

    @staticmethod
    def _validate_radius(radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius < 0:
            raise ValueError("Radius cannot be negative")

    def area(self):
        return math.pi * self.radius ** 2

def calculate_circle_area(radius):
    try:
        circle = Circle(radius)
        return circle.area()
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_radius = 10.0
    area = calculate_circle_area(sample_radius)
    if area is not None:
        print(f"The area of the circle with radius {sample_radius} is {area:.2f}")