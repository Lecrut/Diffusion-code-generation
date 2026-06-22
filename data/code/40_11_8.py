def surface_area_cuboid(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    l = 3
    w = 4
    h = 5
    result = surface_area_cuboid(l, w, h)
    print(result)