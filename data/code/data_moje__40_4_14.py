def calculate_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    length = 5.0
    width = 3.0
    height = 4.0
    area = calculate_surface_area(length, width, height)
    print(area)