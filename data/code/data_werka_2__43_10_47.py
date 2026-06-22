def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    sample_values = [4.5, 6, -2, 'b']
    for value in sample_values:
        try:
            print(calculate_square_area(value))
        except (TypeError, ValueError) as e:
            print(f"Error with value {value}: {e}")