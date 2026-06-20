def is_zero(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or float.")
    return value == 0

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(5))
    print(is_zero(-3))
    print(is_zero(0.0))