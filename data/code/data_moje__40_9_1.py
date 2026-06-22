def surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    a = 1.5
    b = 2.5
    c = 3.5
    print(surface_area(a, b, c))