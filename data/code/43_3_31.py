def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)) or side_length <= 0:
        raise ValueError("Side length must be a positive number")

def square_area(side_length):
    validate_side_length(side_length)
    return side_length ** 2

if __name__ == '__main__':
    sample_values = [3, 4.5, 7]
    for value in sample_values:
        try:
            print(f"Area of square with side {value}: {square_area(value)}")
        except ValueError as e:
            print(e)