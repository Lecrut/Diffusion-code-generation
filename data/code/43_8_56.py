def validate_side_length(side):
    if not isinstance(side, (int, float)) or side <= 0:
        raise ValueError("Side length must be a positive number")

def calculate_square_area(side):
    validate_side_length(side)
    return side ** 2

if __name__ == '__main__':
    sample_values = [3, 5.5, -1, 'a']
    for value in sample_values:
        try:
            print(f"Area of square with side {value}: {calculate_square_area(value)}")
        except ValueError as e:
            print(f"Error: {e}")