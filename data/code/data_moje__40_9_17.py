def calculate_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    l, w, h = 1.5, 2.5, 3.5
    area = calculate_surface_area(l, w, h)
    print(area)