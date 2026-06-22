import math

class SquarePyramid:
    def __init__(self, base_side, height):
        if base_side <= 0 or height <= 0:
            raise ValueError("Base side and height must be positive numbers")
        self.base_side = base_side
        self.height = height

    def calculate_slant_height(self):
        return math.sqrt((self.base_side / 2) ** 2 + self.height ** 2)

    def surface_area(self):
        base_area = self.base_side ** 2
        slant_height = self.calculate_slant_height()
        lateral_area = 2 * self.base_side * slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    pyramid = SquarePyramid(10, 12)
    result = pyramid.surface_area()
    print(result)