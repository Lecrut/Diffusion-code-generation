def calculate_surface_area(base_side: float, slant_height: float) -> float:
    return base_side * base_side + 2 * base_side * slant_height

if __name__ == '__main__':
    print(calculate_surface_area(5.0, 7.0))