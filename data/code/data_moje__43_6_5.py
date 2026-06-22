def surface_area_square_pyramid(base_edge, slant_height):
    base_area = base_edge ** 2
    lateral_area = 4 * (0.5 * base_edge * slant_height)
    return base_area + lateral_area

if __name__ == '__main__':
    edge = 4
    slant = 3
    print(surface_area_square_pyramid(edge, slant))