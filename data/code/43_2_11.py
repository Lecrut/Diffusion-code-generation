class SquarePyramid:
    def __init__(self, base_side, slant_height):
        self.base_side = base_side
        self.slant_height = slant_height

    def surface_area(self):
        base_area = self.base_side ** 2
        lateral_area = 2 * self.base_side * self.slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    pyramid = SquarePyramid(10, 15)
    print(pyramid.surface_area())