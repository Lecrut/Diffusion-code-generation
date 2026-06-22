import math

def surface_area_of_square_pyramid(base_side, perpendicular_height):
    if base_side <= 0 or perpendicular_height <= 0:
        raise ValueError("Base side and perpendicular height must be positive.")
    
    half_base = base_side / 2
    slant_height = math.sqrt(half_base ** 2 + perpendicular_height ** 2)
    
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base_side_value = 10
    height_value = 12
    result = surface_area_of_square_pyramid(base_side_value, height_value)
    print(result)