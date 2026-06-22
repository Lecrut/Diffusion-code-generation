def surface_area_square_pyramid(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base = 4
    slant = 5
    print(surface_area_square_pyramid(base, slant))