def validate_positive(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Side length must be a number")
    if value < 0:
        raise ValueError("Side length must be non-negative")
    return value

def calculate_square_area(side_length):
    validated_side = validate_positive(side_length)
    return validated_side ** 2

if __name__ == '__main__':
    target_side = 50
    computed_area = calculate_square_area(target_side)
    print(computed_area)