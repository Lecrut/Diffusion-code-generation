import math

def square_pyramid_surface_area(base_side: float, vertical_height: float) -> float:
    base_area = base_side * base_side
    slant_height = math.sqrt((base_side / 2) ** 2 + vertical_height ** 2)
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_side_value = 6.0
    height_value = 4.0
    result = square_pyramid_surface_area(base_side_value, height_value)
    print(result)