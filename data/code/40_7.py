def calculate_rectangular_box_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 10.0
    width = 5.0
    height = 2.0
    area = calculate_rectangular_box_surface_area(length, width, height)
    print(area)