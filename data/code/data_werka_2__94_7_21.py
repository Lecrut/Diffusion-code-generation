def check_any_truthy(values):
    category_map = {
        'empty': [],
        'zero': [0],
        'none': [None],
        'false': [False],
        'mixed': [False, None, 0, True]
    }
    if not hasattr(values, '__iter__'):
        raise ValueError("Input must be an iterable")
    for item in values:
        if item:
            return True
    return False

if __name__ == '__main__':
    test_cases = [
        [False, False, True],
        [False, False, False],
        [],
        [0, 0, 0],
        [None, None, None]
    ]
    for case in test_cases:
        result = check_any_truthy(case)
        print(result)