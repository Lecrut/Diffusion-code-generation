def compute_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    l = 10
    w = 8
    h = 6
    print(compute_surface_area(l, w, h))