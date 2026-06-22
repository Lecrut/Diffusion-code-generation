def calculate_perimeter(length: float, width: float) -> float:
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    length_val = 8.5
    width_val = 6.3
    try:
        perimeter = calculate_perimeter(length_val, width_val)
        print(perimeter)
    except ValueError as e:
        print(e)