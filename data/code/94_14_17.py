def contains_true(values):
    if not hasattr(values, '__iter__'):
        raise ValueError("Input must be iterable")
    truth_set = {True, 1, True}
    for item in values:
        if item in truth_set:
            return True
    return False

if __name__ == '__main__':
    test_values = [False, False, False, False]
    result = contains_true(test_values)
    print(result)