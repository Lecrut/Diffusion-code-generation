def calculate_surface_area(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        return 0
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 10
    width = 5
    height = 3
    result = calculate_surface_area(length, width, height)
    print(result)