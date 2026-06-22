class PyramidUtils:
    @staticmethod
    def calculate_square_pyramid_surface_area(base_length, slant_height):
        base_area = base_length * base_length
        lateral_area = 2 * base_length * slant_height
        total_surface_area = base_area + lateral_area
        return total_surface_area

if __name__ == '__main__':
    base_len = 5
    slant_h = 8
    result = PyramidUtils.calculate_square_pyramid_surface_area(base_len, slant_h)
    print(result)