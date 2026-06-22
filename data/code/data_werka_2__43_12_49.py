def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length ** 2

if __name__ == '__main__':
    sample_values = [4, 6.5, -1]
    for value in sample_values:
        try:
            area = calculate_square_area(value)
            print(f"The area of a square with side length {value} is {area}")
        except ValueError as e:
            print(e)