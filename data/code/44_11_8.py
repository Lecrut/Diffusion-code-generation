def calculate_perimeter(length: float, width: float) -> float:
    return 2 * (length + width)

if __name__ == '__main__':
    length_val = 15.0
    width_val = 8.5
    perimeter = calculate_perimeter(length_val, width_val)
    print(perimeter)