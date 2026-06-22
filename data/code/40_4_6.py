def calculate_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    l = 10
    w = 5
    h = 3
    area = calculate_surface_area(l, w, h)
    print(area)