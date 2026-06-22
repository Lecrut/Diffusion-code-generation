def surface_area_square_pyramid(base_side: float, slant_height: float) -> float:
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area
if __name__ == '__main__':
    sample_base_side = 5.0
    sample_slant_height = 6.0
    area = surface_area_square_pyramid(sample_base_side, sample_slant_height)
    print(area)