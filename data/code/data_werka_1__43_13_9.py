def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length <= 0:
        raise ValueError("Side length must be positive")

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length * side_length

if __name__ == '__main__':
    sample_values = [2, 4.5, 6]
    for side in sample_values:
        area = calculate_square_area(side)
        print(f"The area of the square with side length {side} is: {area}")