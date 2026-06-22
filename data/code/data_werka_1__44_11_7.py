def calculate_perimeter(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numeric values.")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        length_val = 8.5
        width_val = 3.2
        perimeter = calculate_perimeter(length_val, width_val)
        print(perimeter)
    except Exception as e:
        print(e)