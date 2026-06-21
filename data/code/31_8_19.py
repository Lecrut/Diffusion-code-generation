import math

def _validate_side(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length must be non-negative")
    return float(side_length)

def calculate_square_area(side_length):
    validated_side = _validate_side(side_length)
    return math.pow(validated_side, 2)

if __name__ == '__main__':
    sample_side = 7.3
    result = calculate_square_area(sample_side)
    print(result)