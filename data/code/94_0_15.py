def validate_boolean_sequence(input_sequence):
    if not hasattr(input_sequence, '__iter__'):
        raise ValueError("Input must be an iterable sequence")
    for index, element in enumerate(input_sequence):
        if not isinstance(element, bool):
            raise ValueError(f"Element at index {index} is not a boolean")
    return True

def verify_any_true(input_sequence):
    validate_boolean_sequence(input_sequence)
    return any(input_sequence)

if __name__ == '__main__':
    test_data = [False, False, False]
    output = verify_any_true(test_data)
    print(output)