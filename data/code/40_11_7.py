def compute_cuboid_surface_area(length, width, height):
    return 2 * (length * width + width * height + length * height)

if __name__ == '__main__':
    l, w, h = 3, 4, 5
    print(compute_cuboid_surface_area(l, w, h))