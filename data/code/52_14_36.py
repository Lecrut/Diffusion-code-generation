def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length ** 2

if __name__ == '__main__':
    sample_side_length = 4
    area = calculate_square_area(sample_side_length)
    print(area)

    another_sample_side_length = 9
    another_area = calculate_square_area(another_sample_side_length)
    print(another_area)