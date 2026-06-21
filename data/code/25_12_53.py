def is_zero(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or float")
    return value == 0

if __name__ == '__main__':
    test_values = [
        0,
        1,
        -1,
        0.0,
        -0.0,
        1e-308,
        1e-309,
        '0',
        None
    ]
    
    for val in test_values:
        try:
            print(f"is_zero({val}): {is_zero(val)}")
        except ValueError as e:
            print(f"is_zero({val}): Error - {e}")