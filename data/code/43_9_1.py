import math

class GeometryUtils:
    @staticmethod
    def calculate_square_pyramid_surface_area(base_side, slant_height):
        if base_side <= 0 or slant_height <= 0:
            raise ValueError("Base side and slant height must be positive")
        base_area = base_side * base_side
        lateral_area = 4 * (0.5 * base_side * slant_height)
        return base_area + lateral_area

if __name__ == '__main__':
    result = GeometryUtils.calculate_square_pyramid_surface_area(4, 5)
    print(result)
    result2 = GeometryUtils.calculate_square_pyramid_surface_area(2, 3)
    print(result2)
    result3 = GeometryUtils.calculate_square_pyramid_surface_area(10, 10)
    print(result3)