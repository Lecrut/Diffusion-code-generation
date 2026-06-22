def check_any_true(values):
    status_map = {True: 'present', False: 'absent'}
    for val in values:
        if val:
            yield True
            return
    yield False

if __name__ == '__main__':
    test_cases = {
        'mixed': [False, False, True, False],
        'none': [False, False, False],
        'start': [True, False, True],
        'empty': []
    }
    for name, seq in test_cases.items():
        result = next(check_any_true(seq))
        print(f"{name}: {result}")