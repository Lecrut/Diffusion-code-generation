def compute_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    length_value = 15
    width_value = 7
    perimeter_result = compute_perimeter(length_value, width_value)
    print(perimeter_result)