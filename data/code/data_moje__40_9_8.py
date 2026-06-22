def calculate_surface_area(width, height, length):
    return 2 * (width * height + width * length + height * length)

if __name__ == '__main__':
    result = calculate_surface_area(1.5, 2.5, 3.5)
    print(result)