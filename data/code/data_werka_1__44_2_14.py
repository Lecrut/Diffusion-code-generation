def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    length_value = 15
    width_value = 8
    calculated_perimeter = calculate_perimeter(length_value, width_value)
    print(calculated_perimeter)