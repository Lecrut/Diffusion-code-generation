import math

def square_pyramid_surface_area(base_side, perpendicular_height):
    if base_side <= 0 or perpendicular_height < 0:
        raise ValueError("Base side must be positive and height must be non-negative.")
    
    if perpendicular_height == 0:
        return base_side * base_side
    
    half_base = base_side / 2.0
    slant_height = math.sqrt(perpendicular_height ** 2 + half_base ** 2)
    
    base_area = base_side ** 2
    triangular_face_area = 0.5 * base_side * slant_height
    lateral_area = 4 * triangular_face_area
    
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base_side_value = 6
    height_value = 4
    area = square_pyramid_surface_area(base_side_value, height_value)
    print(area)