import math

class GeometryUtils:
    @staticmethod
    def calculate_square_pyramid_surface_area(base_side, slant_height):
        base_area = base_side ** 2
        lateral_area = 2 * base_side * slant_height
        total_surface_area = base_area + lateral_area
        return total_surface_area

if __name__ == '__main__':
    side_length = 4
    slant = 5
    result = GeometryUtils.calculate_square_pyramid_surface_area(side_length, slant)
    print(result)