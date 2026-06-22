import math

def surface_area_square_pyramid(base_side, perpendicular_height):
    if base_side <= 0 or perpendicular_height < 0:
        raise ValueError("Base side must be positive and height must be non-negative")
    
    base_area = base_side ** 2
    
    slant_height = math.sqrt((base_side / 2) ** 2 + perpendicular_height ** 2)
    
    lateral_area = 4 * (0.5 * base_side * slant_height)
    
    total_surface_area = base_area + lateral_area
    
    return total_surface_area

if __name__ == '__main__':
    base_side = 4
    perpendicular_height = 6
    result = surface_area_square_pyramid(base_side, perpendicular_height)
    print(result)