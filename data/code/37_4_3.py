def get_parallelogram_area(base, height):
    if not isinstance(base, (int, float, complex)):
        raise TypeError("base must be a numeric type")
    if not isinstance(height, (int, float, complex)):
        raise TypeError("height must be a numeric type")
    if base <= 0:
        raise ValueError("base must be positive")
    if height <= 0:
        raise ValueError("height must be positive")
    return base * height

if __name__ == '__main__':
    try:
        result = get_parallelogram_area(7.5, 4.0)
        print(result)
    except (TypeError, ValueError) as e:
        print(e)