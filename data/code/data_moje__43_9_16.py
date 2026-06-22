import math

class GeometryUtilities:

    @staticmethod
    def calculate_square_pyramid_surface_area(base_side, slant_height):
        base_area = base_side ** 2
        triangular_faces_area = 2 * base_side * slant_height
        total_surface_area = base_area + triangular_faces_area
        return total_surface_area

if __name__ == '__main__':
    base_side_length = 10
    slant_height_value = 12
    result = GeometryUtilities.calculate_square_pyramid_surface_area(base_side_length, slant_height_value)
    print(result)