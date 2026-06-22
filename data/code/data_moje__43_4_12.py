def compute_pyramid_surface_area(base_side, slant_height):
    if base_side <= 0 or slant_height <= 0:
        return 0.0
    base_area = base_side * base_side
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    side_value = 6.0
    height_value = 8.0
    print(compute_pyramid_surface_area(side_value, height_value))