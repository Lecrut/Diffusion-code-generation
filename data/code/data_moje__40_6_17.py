def _compute_pair_product(a, b):
    return a * b

def rectangular_prism_surface_area(length, width, height):
    area_xy = _compute_pair_product(length, width)
    area_yz = _compute_pair_product(width, height)
    area_zx = _compute_pair_product(height, length)
    return 2 * (area_xy + area_yz + area_zx)

if __name__ == '__main__':
    sample_length = 10.75
    sample_width = 4.25
    sample_height = 8.5
    computed_area = rectangular_prism_surface_area(sample_length, sample_width, sample_height)
    print(computed_area)