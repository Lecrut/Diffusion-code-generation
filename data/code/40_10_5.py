def calculate_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 10
    width = 5
    height = 3
    area = calculate_surface_area(length, width, height)
    print(area)