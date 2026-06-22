def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 4 * (0.5 * base_side * slant_height)
    total_surface_area = base_area + lateral_area
    return round(total_surface_area, 2)

if __name__ == '__main__':
    base_side = 4
    slant_height = 6
    result = calculate_square_pyramid_surface_area(base_side, slant_height)
    print(result)