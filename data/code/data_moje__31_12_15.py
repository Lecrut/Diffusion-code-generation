def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length must be non-negative")
    return side_length

def calculate_square_area(side_length):
    validated_side = validate_side_length(side_length)
    return validated_side * validated_side

if __name__ == '__main__':
    side = 7
    area = calculate_square_area(side)
    print(area)