def boolean_negation_logic(input_value):
    if not isinstance(input_value, bool):
        raise ValueError("Input must be a boolean")
    lookup_table = {True: False, False: True}
    return lookup_table[input_value]

if __name__ == '__main__':
    test_cases = [True, False]
    for val in test_cases:
        negated_val = boolean_negation_logic(val)
        print(f"Original: {val}, Negated: {negated_val}")