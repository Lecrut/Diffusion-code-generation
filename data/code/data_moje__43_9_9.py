import math

class GeometryUtils:
    @staticmethod
    def calculate_square_pyramid_surface_area(base_edge, slant_height):
        base_area = base_edge ** 2
        lateral_area = 2 * base_edge * slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    result = GeometryUtils.calculate_square_pyramid_surface_area(4, 5)
    print(result)