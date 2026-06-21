import math

class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        if not (isinstance(base, (int, float)) and isinstance(height, (int, float))):
            raise ValueError("Base and height must be numbers.")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")

    def calculate_hypotenuse(self):
        return math.sqrt(self.base**2 + self.height**2)

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle = RightTriangle(6.0, 8.0)
    hypotenuse = triangle.calculate_hypotenuse()
    area = triangle.calculate_area()
    print(f"Hypotenuse: {hypotenuse}")
    print(f"Area: {area}")