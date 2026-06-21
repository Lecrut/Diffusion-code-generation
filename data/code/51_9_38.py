def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    length_value = 8
    width_value = 6
    result = calculate_perimeter(length_value, width_value)
    print(result)