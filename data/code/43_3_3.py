import math

def calculate_square_pyramid_surface_area(base_side, perpendicular_height):
    if base_side <= 0 or perpendicular_height <= 0:
        raise ValueError("Base side and perpendicular height must be positive numbers")
    
    base_area = base_side ** 2
    slant_height = math.sqrt((base_side / 2) ** 2 + perpendicular_height ** 2)
    lateral_area = 4 * (0.5 * base_side * slant_height)
    total_surface_area = base_area + lateral_area
    
    return total_surface_area

if __name__ == '__main__':
    base_side = 4
    perpendicular_height = 6
    surface_area = calculate_square_pyramid_surface_area(base_side, perpendicular_height)
    print(surface_area)