def calculate_surface_area(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("All dimensions must be positive numbers")
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    length = 5.5
    width = 3.2
    height = 2.8
    area = calculate_surface_area(length, width, height)
    print(area)