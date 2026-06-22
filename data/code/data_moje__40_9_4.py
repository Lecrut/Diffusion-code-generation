def calculate_box_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    length = 1.5
    width = 2.5
    height = 3.5
    result = calculate_box_surface_area(length, width, height)
    print(result)