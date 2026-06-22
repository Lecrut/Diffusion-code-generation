import math

class SquarePyramid:
    def __init__(self, base_side, perpendicular_height):
        if base_side <= 0 or perpendicular_height <= 0:
            raise ValueError("Base side and perpendicular height must be positive numbers.")
        self.base_side = base_side
        self.perpendicular_height = perpendicular_height

    def get_slant_height(self):
        return math.sqrt((self.base_side / 2) ** 2 + self.perpendicular_height ** 2)

    def get_surface_area(self):
        slant_height = self.get_slant_height()
        base_area = self.base_side ** 2
        lateral_area = 2 * self.base_side * slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    pyramid = SquarePyramid(4.0, 3.0)
    print(pyramid.get_surface_area())
    pyramid_small = SquarePyramid(10, 12)
    print(pyramid_small.get_surface_area())