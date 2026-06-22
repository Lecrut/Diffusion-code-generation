def contains_truthy(iterable):
    if isinstance(iterable, str):
        raise ValueError("Strings are not supported as iterable input")
    try:
        iterator = iter(iterable)
    except TypeError:
        raise ValueError("Input must be an iterable")
    return any(iterator)

if __name__ == '__main__':
    test_cases = [
        [0, 0, 0],
        [0, 1, 0],
        [],
        [None, False, 0],
        [None, False, 1],
        [0, 0, 0, 0]
    ]
    for case in test_cases:
        print(contains_truthy(case))
    try:
        contains_truthy("abc")
    except ValueError:
        print(False)