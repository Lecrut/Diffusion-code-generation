TRUE_VALUE = True
FALSE_VALUE = False

def contains_truthy(iterable):
    return any(iterable)

if __name__ == '__main__':
    test_cases = [
        [0, 0, 0],
        [0, 1, 0],
        [],
        [None, FALSE_VALUE, 0],
        [None, FALSE_VALUE, TRUE_VALUE],
        [0, 0, 0, 0]
    ]
    for case in test_cases:
        print(contains_truthy(case))