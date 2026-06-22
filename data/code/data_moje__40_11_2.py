def surface_area_cuboid(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 5
    width = 3
    height = 4
    print(surface_area_cuboid(length, width, height))