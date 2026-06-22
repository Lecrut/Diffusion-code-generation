import math

def calculate_surface_area_of_square_pyramid(base_side, height):
    if base_side <= 0 or height <= 0:
        raise ValueError("Base side and height must be positive numbers.")
    
    half_base = base_side / 2
    slant_height = math.sqrt(height ** 2 + half_base ** 2)
    
    base_area = base_side ** 2
    lateral_area = 4 * (0.5 * base_side * slant_height)
    
    return base_area + lateral_area

if __name__ == '__main__':
    base_side = 4
    height = 3
    
    result = calculate_surface_area_of_square_pyramid(base_side, height)
    print(result)