import math

def surface_area_square_pyramid(base_side, slant_height):
    if base_side <= 0:
        raise ValueError("Base side must be positive.")
    if slant_height <= 0:
        raise ValueError("Slant height must be positive.")
    
    base_area = base_side * base_side
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    b = 4.0
    s = 5.0
    result = surface_area_square_pyramid(b, s)
    print(result)