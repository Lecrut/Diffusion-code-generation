def validate_boolean_sequence(input_sequence):
    if not hasattr(input_sequence, '__iter__'):
        raise ValueError("Input must be iterable")
    for item in input_sequence:
        if not isinstance(item, bool):
            raise ValueError("All elements must be boolean type")
    return True

def invert_truth_sequence(bool_sequence):
    if not validate_boolean_sequence(bool_sequence):
        return []
    return [not element for element in bool_sequence]

if __name__ == '__main__':
    test_data = [True, False, True, False, True]
    computed_result = invert_truth_sequence(test_data)
    print(computed_result)