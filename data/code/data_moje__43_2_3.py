import math

class SquarePyramid:
    def __init__(self, base_side, slant_height):
        if base_side <= 0 or slant_height <= 0:
            raise ValueError("Base side and slant height must be positive.")
        self.base_side = base_side
        self.slant_height = slant_height

    def surface_area(self):
        base_area = self.base_side ** 2
        lateral_area = 2 * self.base_side * self.slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    pyramid = SquarePyramid(base_side=4, slant_height=5)
    print(pyramid.surface_area())