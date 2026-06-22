def calculate_square_pyramid_surface_area(base_side, slant_height):
    if base_side <= 0 or slant_height <= 0:
        raise ValueError("Base side and slant height must be positive numbers.")
    if slant_height <= base_side / 2:
        raise ValueError("Slant height must be greater than half the base side length to form a valid pyramid.")
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_length = 10.0
    slant_length = 13.0
    result = calculate_square_pyramid_surface_area(base_length, slant_length)
    print(result)