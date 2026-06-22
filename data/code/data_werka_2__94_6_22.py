def check_any_true(boolean_sequence):
    if not hasattr(boolean_sequence, '__iter__'):
        raise ValueError("Input must be iterable")
    for element in boolean_sequence:
        if element is True:
            return True
    return False

if __name__ == '__main__':
    sample_data = [False, False, False, True, False]
    result = check_any_true(sample_data)
    print(result)