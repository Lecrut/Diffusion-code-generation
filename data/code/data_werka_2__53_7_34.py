def is_valid_side_length(side_length):
    return isinstance(side_length, (int, float)) and side_length >= 0

def calculate_square_area(side_length):
    if not is_valid_side_length(side_length):
        raise ValueError("Side length must be a non-negative number")
    return side_length * side_length

if __name__ == '__main__':
    sample_values = [4, 10.25, 0, -3]
    for value in sample_values:
        try:
            area = calculate_square_area(value)
            print(f"The area of a square with side length {value} is {area}")
        except ValueError as e:
            print(e)