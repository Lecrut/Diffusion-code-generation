def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)) or side_length <= 0:
        raise ValueError("Side length must be a positive number")

square_area = lambda side_length: side_length ** 2

if __name__ == '__main__':
    sample_values = [2.5, 3.7, 4.8]
    for value in sample_values:
        validate_side_length(value)
        print(f"Area of square with side {value}: {square_area(value)}")