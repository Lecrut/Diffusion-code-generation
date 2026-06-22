def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)) or side_length <= 0:
        raise ValueError("Side length must be a positive number")

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length * side_length

if __name__ == '__main__':
    sample_side_length = 5
    area = calculate_square_area(sample_side_length)
    print(f"The area of the square with side length {sample_side_length} is: {area}")