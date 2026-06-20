ZERO_TOLERANCE = 1e-9

def is_zero(value):
    if isinstance(value, int):
        return value == 0
    elif isinstance(value, float):
        return abs(value) < ZERO_TOLERANCE
    else:
        raise TypeError("Unsupported type for zero check")

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(0.0))
    print(is_zero(-0))
    print(is_zero(-0.0))
    print(is_zero(1))
    print(is_zero(1.0))