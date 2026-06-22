def invert_boolean_sequence(input_sequence):
    if not isinstance(input_sequence, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    
    result = []
    for item in input_sequence:
        if not isinstance(item, bool):
            raise ValueError("All elements must be boolean values")
        result.append(not item)
    return result

if __name__ == '__main__':
    test_data = [True, True, False, False, True]
    output = invert_boolean_sequence(test_data)
    print(output)