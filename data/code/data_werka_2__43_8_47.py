def validate_side_length(side):
    if not isinstance(side, (int, float)) or side <= 0:
        raise ValueError("Side length must be a positive number")

def calculate_square_area(side):
    validate_side_length(side)
    return side ** 2

if __name__ == '__main__':
    sample_values = [3.5, 7, 10]
    for side in sample_values:
        try:
            print(f"Area of square with side {side}: {calculate_square_area(side)}")
        except ValueError as e:
            print(e)