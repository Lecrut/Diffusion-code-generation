def validate_side_length(side):
    if side <= 0:
        raise ValueError("Side length must be positive")
    return True

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length ** 2

if __name__ == '__main__':
    sample_side = 7.5
    area = calculate_square_area(sample_side)
    print(f"The area of a square with side length {sample_side} is {area}")