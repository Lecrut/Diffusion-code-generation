def surface_area_square_pyramid(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    result = surface_area_square_pyramid(4, 5)
    print(result)