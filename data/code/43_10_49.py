SQUARE_UNIT = "square units"

def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    area = side_length * side_length
    return f"{area} {SQUARE_UNIT}"

if __name__ == '__main__':
    sample_values = [4, 8.25, -3, 'b']
    for value in sample_values:
        try:
            print(calculate_square_area(value))
        except (TypeError, ValueError) as e:
            print(f"Error with value {value}: {e}")