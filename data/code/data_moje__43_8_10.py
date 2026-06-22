def calculate_square_pyramid_surface_area(base_side, slant_height):
    if not isinstance(base_side, (int, float)) or not isinstance(slant_height, (int, float)):
        raise TypeError("Base side and slant height must be numbers")
    if base_side <= 0:
        raise ValueError("Base side must be a positive number")
    if slant_height <= 0:
        raise ValueError("Slant height must be a positive number")
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    result = calculate_square_pyramid_surface_area(4, 5)
    print(result)