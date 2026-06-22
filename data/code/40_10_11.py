def calculate_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    result = calculate_surface_area(10, 5, 3)
    print(result)