def check_any_true(values):
    if not hasattr(values, '__iter__'):
        raise ValueError("Input must be iterable")
    for item in values:
        if item is not False and item is not True:
            raise ValueError("All elements must be boolean values")
    return any(values)

if __name__ == '__main__':
    test_input = [False, False, True, False]
    outcome = check_any_true(test_input)
    print(outcome)