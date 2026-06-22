class PyramidUtils:
    @staticmethod
    def calculate_square_pyramid_surface_area(base_length, slant_height):
        if base_length <= 0 or slant_height <= 0:
            raise ValueError("Dimensions must be positive")
        base_area = base_length ** 2
        lateral_area = 2 * base_length * slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    base_len = 10
    slant_h = 12
    result = PyramidUtils.calculate_square_pyramid_surface_area(base_len, slant_h)
    print(result)
    
    base_len_2 = 5
    slant_h_2 = 8
    result_2 = PyramidUtils.calculate_square_pyramid_surface_area(base_len_2, slant_h_2)
    print(result_2)