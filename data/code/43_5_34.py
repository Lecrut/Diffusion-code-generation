def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a number")
    if side_length <= 0:
        raise ValueError("Side length must be positive")

def area_of_square(side_length):
    validate_side_length(side_length)
    return side_length ** 2

if __name__ == '__main__':
    sample_side_length = 6
    print(area_of_square(sample_side_length))