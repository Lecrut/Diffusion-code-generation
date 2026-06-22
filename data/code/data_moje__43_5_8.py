import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    triangular_face_area = 0.5 * base_side * slant_height
    total_lateral_area = 4 * triangular_face_area
    return base_area + total_lateral_area

if __name__ == '__main__':
    base_length = 10
    slant = 12
    result = calculate_square_pyramid_surface_area(base_length, slant)
    print(result)