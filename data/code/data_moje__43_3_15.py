import math

def surface_area_square_pyramid(base_side, height):
    if base_side <= 0 or height <= 0:
        raise ValueError("Base side and height must be positive")
    
    slant_height = math.sqrt((base_side / 2) ** 2 + height ** 2)
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    result = surface_area_square_pyramid(4, 6)
    print(result)