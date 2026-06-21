def invert_boolean(input_value):
    if not isinstance(input_value, bool):
        raise ValueError("Input must be a boolean value")
    return bool(1 - int(input_value))

if __name__ == '__main__':
    test_cases = [True, False]
    for case in test_cases:
        inverted = invert_boolean(case)
        print(inverted)