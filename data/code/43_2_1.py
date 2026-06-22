import math

class SquarePyramid:
    def __init__(self, base_side: float, slant_height: float):
        self.base_side = base_side
        self.slant_height = slant_height

    def surface_area(self) -> float:
        base_area = self.base_side ** 2
        lateral_area = 2 * self.base_side * self.slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    pyramid = SquarePyramid(10.0, 12.0)
    area = pyramid.surface_area()
    print(area)