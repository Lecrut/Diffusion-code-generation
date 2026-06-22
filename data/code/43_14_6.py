def compute_square_pyramid_surface_area(base_side, slant_height):
    if base_side <= 0 or slant_height <= 0:
        raise ValueError('Base side and slant height must be positive numbers.')
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area
if __name__ == '__main__':
    base_side = 4.0
    slant_height = 5.0
    surface_area = compute_square_pyramid_surface_area(base_side, slant_height)
    print(surface_area)