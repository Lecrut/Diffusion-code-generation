def calculate_rectangle_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    length_value = 15
    width_value = 7
    result = calculate_rectangle_perimeter(length_value, width_value)
    print(result)