def cuboid_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    print(cuboid_surface_area(5, 3, 4))