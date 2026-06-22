def pyramid_surface_area(base_side, slant_height):
    if base_side <= 0 or slant_height <= 0:
        raise ValueError("Dimensions must be positive")
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return round(base_area + lateral_area, 2)

if __name__ == '__main__':
    sample_base = 4.5
    sample_slant = 7.2
    area = pyramid_surface_area(sample_base, sample_slant)
    print(area)