def validate_bool_sequence(input_data):
    if not isinstance(input_data, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    for index, element in enumerate(input_data):
        if not isinstance(element, bool):
            raise ValueError(f"Element at index {index} is not a boolean")
    return True

def has_true_value(bool_sequence):
    validate_bool_sequence(bool_sequence)
    return any(bool_sequence)

if __name__ == '__main__':
    test_data = [False, False, False, True, False]
    output = has_true_value(test_data)
    print(output)