import math

class SquarePyramid:
    def __init__(self, base_side, slant_height):
        if base_side <= 0 or slant_height <= 0:
            raise ValueError("Base side and slant height must be positive")
        self.base_side = base_side
        self.slant_height = slant_height

    def surface_area(self):
        base_area = self.base_side ** 2
        lateral_area = 4 * (0.5 * self.base_side * self.slant_height)
        return base_area + lateral_area

    def volume(self):
        half_base = self.base_side / 2
        height = math.sqrt(self.slant_height ** 2 - half_base ** 2)
        return (self.base_side ** 2 * height) / 3

if __name__ == '__main__':
    base_side = 6
    slant_height = 5
    pyramid = SquarePyramid(base_side, slant_height)
    print(pyramid.surface_area())