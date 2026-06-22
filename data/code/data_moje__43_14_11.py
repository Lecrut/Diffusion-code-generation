def surface_area_square_pyramid(base_side, slant_height):
    return base_side ** 2 + 2 * base_side * slant_height

if __name__ == '__main__':
    result = surface_area_square_pyramid(4, 5)
    print(result)