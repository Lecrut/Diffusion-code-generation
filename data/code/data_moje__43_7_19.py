def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    triangle_area = 0.5 * base_side * slant_height
    lateral_area = 4 * triangle_area
    total_area = base_area + lateral_area
    return round(total_area, 2)

if __name__ == '__main__':
    base_side = 5.0
    slant_height = 8.0
    result = calculate_square_pyramid_surface_area(base_side, slant_height)
    print(result)