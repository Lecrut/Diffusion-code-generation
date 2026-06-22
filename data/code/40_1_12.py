def calculate_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    l = 5.0
    w = 3.0
    h = 2.0
    result = calculate_surface_area(l, w, h)
    print(result)