import math

class GeometryUtils:
    @staticmethod
    def calculate_square_pyramid_surface_area(base_edge, slant_height):
        base_area = base_edge * base_edge
        triangle_area = 0.5 * base_edge * slant_height
        lateral_area = 4 * triangle_area
        total_surface_area = base_area + lateral_area
        return total_surface_area

if __name__ == '__main__':
    edge_length = 10
    slant_height = 12
    area = GeometryUtils.calculate_square_pyramid_surface_area(edge_length, slant_height)
    print(area)

    edge_length_2 = 6
    slant_height_2 = 8
    area_2 = GeometryUtils.calculate_square_pyramid_surface_area(edge_length_2, slant_height_2)
    print(area_2)