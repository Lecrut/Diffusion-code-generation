def calculate_surface_area(base_side: float, height: float) -> float:
    import math
    slant_height = math.sqrt((base_side / 2) ** 2 + height ** 2)
    lateral_area = 2 * base_side * slant_height
    base_area = base_side ** 2
    return lateral_area + base_area

if __name__ == '__main__':
    base = 10.0
    height = 12.0
    result = calculate_surface_area(base, height)
    print(result)