import math

class SquarePyramid:
    def __init__(self, base_side, perpendicular_height):
        if base_side <= 0:
            raise ValueError("Base side must be positive")
        if perpendicular_height <= 0:
            raise ValueError("Perpendicular height must be positive")
        self.base_side = base_side
        self.perpendicular_height = perpendicular_height

    def get_slant_height(self):
        half_base = self.base_side / 2.0
        return math.sqrt(half_base ** 2 + self.perpendicular_height ** 2)

    def get_lateral_surface_area(self):
        slant_height = self.get_slant_height()
        return 2 * self.base_side * slant_height

    def get_base_area(self):
        return self.base_side ** 2

    def get_total_surface_area(self):
        return self.get_base_area() + self.get_lateral_surface_area()

if __name__ == '__main__':
    pyramid = SquarePyramid(10.0, 12.0)
    print(pyramid.get_total_surface_area())