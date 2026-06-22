import math

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self._validate_dimensions()

    def _validate_dimensions(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers.")

    def calculate_hypotenuse(self):
        return math.sqrt(self.base**2 + self.height**2)

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle = Triangle(6.0, 8.0)
    hypotenuse = triangle.calculate_hypotenuse()
    area = triangle.calculate_area()
    print(f"Hypotenuse: {hypotenuse}")
    print(f"Area: {area}")