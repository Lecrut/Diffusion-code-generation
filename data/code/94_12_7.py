def has_truthy_value(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be an iterable")
    return any(iterable)

if __name__ == '__main__':
    test_cases = [
        [0, 0, 0],
        [0, 1, 0],
        [],
        [None, False, 0],
        [None, False, 1],
        [False, None, 0],
        [True, 0, 0]
    ]
    for case in test_cases:
        print(has_truthy_value(case))