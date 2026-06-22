import math

def surface_area_square_pyramid(base_side: float, height: float) -> float:
    base_area = base_side ** 2
    slant_height = math.sqrt((base_side / 2) ** 2 + height ** 2)
    lateral_area = base_side * math.sqrt((base_side / 2) ** 2 + height ** 2) * 2
    return base_area + lateral_area

if __name__ == '__main__':
    base_side = 4
    height = 6
    result = surface_area_square_pyramid(base_side, height)
    print(result)