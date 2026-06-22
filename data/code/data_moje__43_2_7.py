import math

class SquarePyramid:
    def __init__(self, base_side, slant_height):
        self.base_side = base_side
        self.slant_height = slant_height

    def surface_area(self):
        base_area = self.base_side ** 2
        lateral_area = 2 * self.base_side * self.slant_height
        return base_area + lateral_area

    def volume(self):
        base_area = self.base_side ** 2
        height = math.sqrt(self.slant_height ** 2 - (self.base_side / 2) ** 2)
        return (1 / 3) * base_area * height

if __name__ == '__main__':
    pyramid = SquarePyramid(base_side=10, slant_height=13)
    area = pyramid.surface_area()
    vol = pyramid.volume()
    print(area)
    print(vol)