import math

def calculate_pyramid_surface_area(base_side: float, slant_height: float) -> float:
    if base_side <= 0:
        raise ValueError("Base side must be positive")
    if slant_height <= 0:
        raise ValueError("Slant height must be positive")
    
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    side_length = 10
    slant_height_val = 12
    total_area = calculate_pyramid_surface_area(side_length, slant_height_val)
    print(total_area)