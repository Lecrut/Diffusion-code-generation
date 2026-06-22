def calculate_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    l = 5
    w = 3
    h = 4
    print(calculate_surface_area(l, w, h))