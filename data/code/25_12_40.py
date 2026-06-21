def is_zero(value):
    def validate_input(val):
        if not isinstance(val, (int, float)):
            raise ValueError("Input must be an integer or a float")
    
    validate_input(value)
    return value == 0

if __name__ == '__main__':
    test_values = [
        0,
        1,
        -0.0,
        0.001,
        1e-308,
        '0',
        None,
        True,
        False
    ]
    
    for val in test_values:
        try:
            print(f"is_zero({val}): {is_zero(val)}")
        except ValueError as e:
            print(f"is_zero({val}): Error - {e}")