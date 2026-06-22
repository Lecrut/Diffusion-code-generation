def calculate_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    print(calculate_surface_area(5, 3, 2))