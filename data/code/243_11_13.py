import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def validate_radius(self):
        if not isinstance(self.radius, (int, float)) or self.radius <= 0:
            raise ValueError("Radius must be a positive number")

    def calculate_perimeter(self):
        self.validate_radius()
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_radius = 5.0
    circle1 = Circle(sample_radius)
    perimeter = circle1.calculate_perimeter()
    print(f"Radius: {sample_radius}")
    print(f"Perimeter: {perimeter}")