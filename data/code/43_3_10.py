import math

def calculate_pyramid_surface_area(base_side, perpendicular_height):
    if base_side <= 0 or perpendicular_height < 0:
        raise ValueError("Base side must be positive and height must be non-negative.")
    half_base = base_side / 2.0
    slant_height = math.sqrt(perpendicular_height ** 2 + half_base ** 2)
    base_area = base_side * base_side
    triangular_face_area = 0.5 * base_side * slant_height
    total_surface_area = base_area + 4 * triangular_face_area
    return total_surface_area

if __name__ == '__main__':
    sample_base = 6.0
    sample_height = 4.0
    result = calculate_pyramid_surface_area(sample_base, sample_height)
    print(result)