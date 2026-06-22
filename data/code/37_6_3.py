def _validate_positive_number(value, name):
    if isinstance(value, bool):
        raise ValueError(f"{name} must be a number")
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be numeric")
    if value <= 0:
        raise ValueError(f"{name} must be positive")

def parallelogram_area(base, height):
    _validate_positive_number(base, "base")
    _validate_positive_number(height, "height")
    return base * height

if __name__ == '__main__':
    result = parallelogram_area(7.5, 4)
    print(result)