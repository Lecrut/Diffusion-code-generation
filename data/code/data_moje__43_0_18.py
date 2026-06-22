def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 4 * (0.5 * base_side * slant_height)
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base = 10.0
    slant = 13.0
    result = calculate_square_pyramid_surface_area(base, slant)
    print(result)