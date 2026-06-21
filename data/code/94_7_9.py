def check_any_truthy(source):
    if isinstance(source, (str, bytes)):
        raise ValueError("String and bytes iterables are not supported as atomic values may be ambiguous.")
    if not hasattr(source, '__iter__'):
        raise TypeError("Input must be an iterable.")
    result = False
    for element in source:
        if element:
            result = True
            break
    return result

if __name__ == '__main__':
    test_cases = [
        [False, False, False],
        [False, True, False],
        [0, 0, 1],
        [None, None, None],
        [],
        [0.0, 0.0, 0.0000001],
        [False, 0, None, ""]
    ]
    for case in test_cases:
        print(check_any_truthy(case))