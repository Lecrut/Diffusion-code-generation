VALID_TYPES = (int, float)
NEGATIVE_MSG = "Dimensions must be non-negative numbers"
TYPE_MSG = "Dimensions must be numeric"

def validate_dimension(value):
    if not isinstance(value, VALID_TYPES):
        raise TypeError(TYPE_MSG)
    if value < 0:
        raise ValueError(NEGATIVE_MSG)
    return value

def compute_area(width, height):
    w = validate_dimension(width)
    h = validate_dimension(height)
    return w * h

def safe_area(width, height):
    try:
        return compute_area(width, height)
    except (TypeError, ValueError):
        return None

if __name__ == '__main__':
    print(compute_area(5, 10))
    print(compute_area(3.5, 2.0))
    print(safe_area("bad", 10))
    print(safe_area(-1, 5))