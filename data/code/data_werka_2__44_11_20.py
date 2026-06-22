PERIMETER_MULTIPLIER = 2

def calculate_perimeter(length, width):
    return PERIMETER_MULTIPLIER * (length + width)

if __name__ == '__main__':
    length_value = 10
    width_value = 4
    perimeter_result = calculate_perimeter(length_value, width_value)
    print(perimeter_result)