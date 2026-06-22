def calculate_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    result = calculate_surface_area(3.5, 4.2, 1.0)
    print(result)