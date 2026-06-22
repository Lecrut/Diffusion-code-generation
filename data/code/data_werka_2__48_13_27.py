import math

class RightTriangle:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def hypotenuse(self):
        return math.sqrt(self._sum_of_squares())

    def area(self):
        return 0.5 * self.base * self.height

    def _sum_of_squares(self):
        return self.base**2 + self.height**2

if __name__ == '__main__':
    triangle = RightTriangle(6.0, 8.0)
    print(f"Hypotenuse: {triangle.hypotenuse()}")
    print(f"Area: {triangle.area()}")