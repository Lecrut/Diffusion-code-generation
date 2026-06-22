def process_boolean(input_value):
    if not isinstance(input_value, bool):
        raise ValueError("Expected a boolean value")
    return not input_value

if __name__ == '__main__':
    test_cases = [True, False]
    for case in test_cases:
        negated = process_boolean(case)
        print(negated)