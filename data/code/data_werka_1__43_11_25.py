def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a numeric value.")
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    return side_length * side_length

if __name__ == '__main__':
    try:
        sample_values = [4.5, 7, 12.3]
        for value in sample_values:
            print(calculate_square_area(value))
    except ValueError as e:
        print(e)