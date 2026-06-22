def surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    l = 3
    w = 4
    h = 5
    print(surface_area(l, w, h))