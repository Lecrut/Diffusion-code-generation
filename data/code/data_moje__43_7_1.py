def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    lateral_area = 2 * base_side * slant_height
    total_area = base_area + lateral_area
    return round(total_area, 2)

if __name__ == '__main__':
    side = 6
    slant = 10
    result = calculate_square_pyramid_surface_area(side, slant)
    print(result)