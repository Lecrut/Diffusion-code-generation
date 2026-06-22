import math

class GeometryUtils:

    @staticmethod
    def surface_area_square_pyramid(base_side, slant_height):
        base_area = base_side * base_side
        lateral_area = 2 * base_side * slant_height
        total_surface_area = base_area + lateral_area
        return total_surface_area

if __name__ == '__main__':
    base = 4
    slant_height = 5
    result = GeometryUtils.surface_area_square_pyramid(base, slant_height)
    print(result)