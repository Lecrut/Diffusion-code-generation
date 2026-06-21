def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    length_value = 6
    width_value = 2
    result = calculate_perimeter(length_value, width_value)
    print(result)