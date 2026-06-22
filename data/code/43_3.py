import math

def calculate_square_pyramid_surface_area(base_side, height):
    if base_side <= 0:
        raise ValueError("Base side must be positive")
    if height < 0:
        raise ValueError("Height must be non-negative")
    
    base_area = base_side ** 2
    half_side = base_side / 2
    slant_height = math.sqrt(height ** 2 + half_side ** 2)
    lateral_area = 4 * (0.5 * base_side * slant_height)
    
    return base_area + lateral_area

if __name__ == '__main__':
    sample_base_side = 4.0
    sample_height = 3.0
    result = calculate_square_pyramid_surface_area(sample_base_side, sample_height)
    print(result)