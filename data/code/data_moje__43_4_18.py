def total_surface_area(base_side, slant_height):
    return base_side * (base_side + 2 * slant_height)

if __name__ == '__main__':
    base = 5.0
    slant = 10.0
    result = total_surface_area(base, slant)
    print(result)