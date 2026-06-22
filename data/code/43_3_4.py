import math

def surface_area_square_pyramid(base_side, height):
    if base_side <= 0:
        raise ValueError("Base side must be positive")
    if height <= 0:
        raise ValueError("Height must be positive")
    
    half_base = base_side / 2.0
    slant_height = math.sqrt(half_base ** 2 + height ** 2)
    
    base_area = base_side ** 2
    lateral_area = 4 * (0.5 * base_side * slant_height)
    
    total_area = base_area + lateral_area
    return total_area

if __name__ == '__main__':
    result = surface_area_square_pyramid(10, 12)
    print(result)