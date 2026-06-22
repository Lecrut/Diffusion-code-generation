def cuboid_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    print(cuboid_surface_area(1, 1, 1))
    print(cuboid_surface_area(2, 3, 4))
    print(cuboid_surface_area(10, 20, 30))