def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)) or side_length < 0:
        raise ValueError("Side length must be a non-negative number")

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return float(side_length ** 2)

if __name__ == '__main__':
    sample_sides = [5.0, 10.5]
    for side in sample_sides:
        area = calculate_square_area(side)
        print(f"The area of the square with side length {side} is {area}")