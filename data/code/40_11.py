def compute_cuboid_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 5
    width = 4
    height = 3
    print(compute_cuboid_surface_area(length, width, height))