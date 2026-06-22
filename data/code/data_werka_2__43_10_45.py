def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    sample_values = {
        'small': 2.5,
        'medium': 7.0,
        'large': 15.0
    }
    for label, value in sample_values.items():
        try:
            print(f"{label}: {calculate_square_area(value)}")
        except (TypeError, ValueError) as e:
            print(f"Error with value {value}: {e}")