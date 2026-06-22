def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length <= 0:
        raise ValueError("Side length must be positive")

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length ** 2

if __name__ == '__main__':
    sample_side_length = 10
    area = calculate_square_area(sample_side_length)
    print(area)