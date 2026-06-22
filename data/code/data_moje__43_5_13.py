import math

class SquarePyramid:
    def __init__(self, base_side, slant_height):
        self.base_side = base_side
        self.slant_height = slant_height

    def get_base_area(self):
        return self.base_side ** 2

    def get_lateral_area(self):
        return 2 * self.base_side * self.slant_height

    def get_total_surface_area(self):
        return self.get_base_area() + self.get_lateral_area()

if __name__ == '__main__':
    py = SquarePyramid(7.5, 8.2)
    print(py.get_base_area())
    print(py.get_lateral_area())
    print(py.get_total_surface_area())