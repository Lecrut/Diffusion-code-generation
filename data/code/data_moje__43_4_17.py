def total_surface_area(base_side, slant_height):
    return base_side ** 2 + 2 * base_side * slant_height

if __name__ == '__main__':
    print(total_surface_area(5, 7))