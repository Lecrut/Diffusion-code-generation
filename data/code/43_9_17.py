class PyramidUtils:
    @staticmethod
    def calculate_surface_area(base_length, slant_height):
        base_area = base_length * base_length
        lateral_area = 2 * base_length * slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    test_base = 4.0
    test_slant = 5.0
    result = PyramidUtils.calculate_surface_area(test_base, test_slant)
    print(result)
    test_base_2 = 10.0
    test_slant_2 = 13.0
    result_2 = PyramidUtils.calculate_surface_area(test_base_2, test_slant_2)
    print(result_2)