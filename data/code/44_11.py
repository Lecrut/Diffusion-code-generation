def calculate_rectangle_perimeter(length: float, width: float) -> float:
    return 2 * (length + width)
if __name__ == '__main__':
    length_val = 10.5
    width_val = 5.0
    perimeter = calculate_rectangle_perimeter(length_val, width_val)
    print(perimeter)