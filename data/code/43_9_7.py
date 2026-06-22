class PyramidUtils:
    @staticmethod
    def calculate_surface_area(base_side, height):
        if base_side <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        slant_height = ((base_side / 2) ** 2 + height ** 2) ** 0.5
        base_area = base_side ** 2
        lateral_area = 2 * base_side * slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    pyramid = PyramidUtils()
    result = pyramid.calculate_surface_area(10, 12)
    print(result)
    result2 = PyramidUtils.calculate_surface_area(4, 3)
    print(result2)