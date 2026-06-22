def check_truthy_values(source):
    if not hasattr(source, '__iter__'):
        raise ValueError("Input must be an iterable")
    return any(source)

if __name__ == '__main__':
    test_cases = [
        [False, 0, None],
        [True, 0, None],
        [0, 0, 0],
        [1, 2, 3]
    ]
    for case in test_cases:
        print(check_truthy_values(case))