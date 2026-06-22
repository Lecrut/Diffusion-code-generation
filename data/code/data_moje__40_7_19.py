def calculate_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 5
    width = 3
    height = 2
    result = calculate_surface_area(length, width, height)
    print(result)