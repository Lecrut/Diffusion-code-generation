import math

class SquarePyramid:
    def __init__(self, base_side, slant_height):
        self.base_side = base_side
        self.slant_height = slant_height

    def calculate_surface_area(self):
        base_area = self.base_side ** 2
        lateral_area = 2 * self.base_side * self.slant_height
        total_surface_area = base_area + lateral_area
        return total_surface_area

if __name__ == '__main__':
    base = 6.0
    slant = 5.0
    pyramid = SquarePyramid(base, slant)
    print(pyramid.calculate_surface_area())