def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length ** 2

if __name__ == '__main__':
    sample_values = [4, 6.5, 12]
    for length in sample_values:
        try:
            area = calculate_square_area(length)
            print(f"The area of a square with side length {length} is {area}")
        except (ValueError, TypeError) as e:
            print(e)