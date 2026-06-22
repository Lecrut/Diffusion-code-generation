def calculate_perimeter(width, height):
    return 2 * (width + height)

if __name__ == '__main__':
    width_value = 10.0
    height_value = 4.5
    perimeter_result = calculate_perimeter(width_value, height_value)
    print(perimeter_result)