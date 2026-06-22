def calculate_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    length = 5
    width = 3
    height = 4
    result = calculate_surface_area(length, width, height)
    print(result)