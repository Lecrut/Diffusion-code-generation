def total_surface_area(base_side, slant_height):
    return base_side ** 2 + 2 * base_side * slant_height

if __name__ == '__main__':
    base = 5.0
    slant = 7.0
    print(total_surface_area(base, slant))