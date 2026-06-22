class PyramidUtility:
    @staticmethod
    def calculate_surface_area(base_side, slant_height):
        base_area = base_side * base_side
        lateral_area = 2 * base_side * slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    test_side = 4
    test_slant = 6
    result = PyramidUtility.calculate_surface_area(test_side, test_slant)
    print(result)