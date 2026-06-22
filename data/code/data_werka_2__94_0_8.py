def has_true_value(bool_sequence):
    if not isinstance(bool_sequence, (list, tuple)):
        raise ValueError("Input must be a list or tuple of booleans")
    for item in bool_sequence:
        if not isinstance(item, bool):
            raise ValueError("All elements must be boolean values")
    return any(bool_sequence)

if __name__ == '__main__':
    test_data = [False, False, True, False]
    output = has_true_value(test_data)
    print(output)