import math

class GeometryUtils:

    @staticmethod
    def square_pyramid_surface_area(base_edge, slant_height):
        base_area = base_edge * base_edge
        lateral_area = 2 * base_edge * slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    base_edge_value = 10.0
    slant_height_value = 15.0
    result = GeometryUtils.square_pyramid_surface_area(base_edge_value, slant_height_value)
    print(result)