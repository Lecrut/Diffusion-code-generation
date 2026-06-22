def invert_logical_state(input_value):
    if not isinstance(input_value, bool):
        raise ValueError("Input must be a boolean value")
    truth_table = {True: False, False: True}
    return truth_table[input_value]

if __name__ == '__main__':
    test_cases = [True, False]
    for case in test_cases:
        inverted = invert_logical_state(case)
        print(inverted)