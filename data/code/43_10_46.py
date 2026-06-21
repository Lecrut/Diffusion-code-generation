def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    sample_values = {
        'tiny': 1.2,
        'medium': 6.75,
        'huge': 15
    }
    for label, value in sample_values.items():
        try:
            area = calculate_square_area(value)
            print(f"{label}: {area}")
        except (TypeError, ValueError) as e:
            print(f"Error with value {value}: {e}")