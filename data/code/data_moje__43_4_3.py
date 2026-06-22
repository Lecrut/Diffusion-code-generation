def total_surface_area(base_side, slant_height):
    return base_side ** 2 + 2 * base_side * slant_height

if __name__ == '__main__':
    side = 4
    height = 5
    print(total_surface_area(side, height))