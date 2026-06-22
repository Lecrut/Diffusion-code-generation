def calculate_square_pyramid_surface_area(base_side, slant_height):
    if not isinstance(base_side, (int, float)):
        raise TypeError("base_side must be a number")
    if not isinstance(slant_height, (int, float)):
        raise TypeError("slant_height must be a number")
    if base_side <= 0:
        raise ValueError("base_side must be positive")
    if slant_height <= 0:
        raise ValueError("slant_height must be positive")
    base_area = base_side * base_side
    lateral_area = 2 * base_side * slant_height
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base = 5.0
    height = 8.0
    result = calculate_square_pyramid_surface_area(base, height)
    print(result)
    base_int = 4
    height_int = 6
    result_int = calculate_square_pyramid_surface_area(base_int, height_int)
    print(result_int)
    try:
        calculate_square_pyramid_surface_area(-1, 5)
    except ValueError as e:
        print(e)
    try:
        calculate_square_pyramid_surface_area(5, 0)
    except ValueError as e:
        print(e)