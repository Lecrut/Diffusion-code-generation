def surface_area_cuboid(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    l = 5
    w = 3
    h = 4
    print(surface_area_cuboid(l, w, h))