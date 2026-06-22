import math

class TriangleGeometry:
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)

    def get_area(self):
        return 0.5 * self.base * self.height

    def get_perimeter_equilateral_approx(self):
        if self.base <= 0 or self.height <= 0:
            return 0
        side = math.sqrt((self.base / 2) ** 2 + self.height ** 2)
        return 3 * side

if __name__ == '__main__':
    my_triangle = TriangleGeometry(base=12.5, height=8.0)
    print(my_triangle.get_area())
    print(my_triangle.get_perimeter_equilateral_approx())