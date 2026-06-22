import math

def calculate_square_pyramid_surface_area(base_side: float, slant_height: float) -> float:
    base_area = base_side ** 2
    triangular_face_area = (1 / 2) * base_side * slant_height
    lateral_area = 4 * triangular_face_area
    total_area = base_area + lateral_area
    return total_area

if __name__ == '__main__':
    side = 10.0
    slant = 12.0
    area = calculate_square_pyramid_surface_area(side, slant)
    print(area)