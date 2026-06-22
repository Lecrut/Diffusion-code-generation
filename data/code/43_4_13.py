def calculate_total_surface_area(base_side: float, slant_height: float) -> float:
    base_area = base_side ** 2
    lateral_area = 4 * (0.5 * base_side * slant_height)
    return base_area + lateral_area

if __name__ == '__main__':
    print(calculate_total_surface_area(10, 13))