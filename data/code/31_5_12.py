DEFAULT_SIDE_LENGTH = 10

def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return side_length

def calculate_square_area(side_length):
    validated_side = validate_side_length(side_length)
    area = validated_side ** 2
    return area

if __name__ == '__main__':
    test_side = DEFAULT_SIDE_LENGTH
    result = calculate_square_area(test_side)
    print(result)