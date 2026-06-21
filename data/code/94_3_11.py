def has_true_element(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input must be iterable")
    for item in sequence:
        if item is True:
            return True
    return False

if __name__ == '__main__':
    test_data = [False, False, True, False]
    output = has_true_element(test_data)
    print(output)