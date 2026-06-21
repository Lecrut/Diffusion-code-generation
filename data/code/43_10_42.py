def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    area = side_length * side_length
    return area

if __name__ == '__main__':
    sample_values = [4.0, 6, -2, 'b']
    for value in sample_values:
        try:
            result = calculate_square_area(value)
            print(f"Area of square with side {value}: {result}")
        except (TypeError, ValueError) as e:
            print(f"Error with value {value}: {e}")