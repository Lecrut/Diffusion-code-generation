def _validate_positive_integer(value):
    if not isinstance(value, int):
        raise TypeError("Side length must be an integer")
    if value < 0:
        raise ValueError("Side length must be non-negative")
    return True

def compute_square(side_length):
    _validate_positive_integer(side_length)
    return side_length * side_length

if __name__ == '__main__':
    sample_side = 7
    area_result = compute_square(sample_side)
    print(area_result)