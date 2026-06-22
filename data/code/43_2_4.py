class SquarePyramid:
    def __init__(self, base_side, slant_height):
        self.base_side = base_side
        self.slant_height = slant_height

    def calculate_surface_area(self):
        base_area = self.base_side * self.base_side
        lateral_area = 2 * self.base_side * self.slant_height
        total_area = base_area + lateral_area
        return total_area

if __name__ == '__main__':
    pyramid = SquarePyramid(10, 15)
    result = pyramid.calculate_surface_area()
    print(result)