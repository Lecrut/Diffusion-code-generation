def calculate_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    result = calculate_surface_area(5.5, 3.2, 2.1)
    print(result)