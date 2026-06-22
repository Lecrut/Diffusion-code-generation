def total_surface_area(base_side: float, slant_height: float) -> float:
    base_area = base_side * base_side
    lateral_area = 4 * (0.5 * base_side * slant_height)
    return base_area + lateral_area
if __name__ == '__main__':
    base_side_val = 4.0
    slant_height_val = 5.0
    result = total_surface_area(base_side_val, slant_height_val)
    print(result)