def calculate_perimeter(length: float, width: float) -> float:
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        length_val = 8.3
        width_val = 2.7
        perimeter = calculate_perimeter(length_val, width_val)
        print(perimeter)
    except ValueError as e:
        print(e)