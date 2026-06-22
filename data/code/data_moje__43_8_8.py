def calculate_square_pyramid_surface_area(base_side, slant_height):
    if base_side <= 0:
        raise ValueError("base_side must be a positive number")
    if slant_height <= 0:
        raise ValueError("slant_height must be a positive number")
    base_area = base_side * base_side
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    side = 4.0
    height = 6.0
    result = calculate_square_pyramid_surface_area(side, height)
    print(result)