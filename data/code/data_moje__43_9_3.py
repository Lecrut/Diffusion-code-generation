class PyramidUtility:
    @staticmethod
    def calculate_square_pyramid_surface_area(base_side, slant_height):
        base_area = base_side * base_side
        lateral_area = 2 * base_side * slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    base = 5
    height = 6
    result = PyramidUtility.calculate_square_pyramid_surface_area(base, height)
    print(result)