import math

class Triangle:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def calculate_hypotenuse(self):
        return math.sqrt(self.base**2 + self.height**2)

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle_dimensions = {
        'base': 6.0,
        'height': 8.0
    }
    triangle = Triangle(triangle_dimensions['base'], triangle_dimensions['height'])
    hypotenuse = triangle.calculate_hypotenuse()
    area = triangle.calculate_area()
    print(f"Hypotenuse: {hypotenuse}")
    print(f"Area: {area}")