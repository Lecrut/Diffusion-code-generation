def total_surface_area(base_side: float, slant_height: float) -> float:
    return base_side ** 2 + 2 * base_side * slant_height

if __name__ == '__main__':
    side = 5.0
    slant = 12.0
    result = total_surface_area(side, slant)
    print(result)