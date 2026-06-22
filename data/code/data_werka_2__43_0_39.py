def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise TypeError("The side length must be a number.")
    if side < 0:
        raise ValueError("The side length cannot be negative.")
    return side * side

if __name__ == '__main__':
    sample_values = {
        'tiny': 1,
        'small': 3,
        'medium': 5,
        'large': 10,
        'huge': 20
    }
    for size, side_length in sample_values.items():
        try:
            area = calculate_square_area(side_length)
            print(f"The area of a {size} square with side length {side_length} is {area}.")
        except (TypeError, ValueError) as e:
            print(e)