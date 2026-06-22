class PyramidUtils:
    @staticmethod
    def calculate_square_pyramid_surface_area(base_side, slant_height):
        if base_side <= 0 or slant_height <= 0:
            raise ValueError("Dimensions must be positive")
        base_area = base_side * base_side
        lateral_area = 2 * base_side * slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    base = 5
    slant = 8
    area = PyramidUtils.calculate_square_pyramid_surface_area(base, slant)
    print(area)
    base_2 = 10
    slant_2 = 13
    area_2 = PyramidUtils.calculate_square_pyramid_surface_area(base_2, slant_2)
    print(area_2)