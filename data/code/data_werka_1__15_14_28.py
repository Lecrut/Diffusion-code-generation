def strict_equals(a, b):
    return type(a) is type(b) and a == b

if __name__ == '__main__':
    test_cases = [
        (1, 1),
        (1, '1'),
        ('1', '1'),
        (1.0, 1),
        (True, 1),
        ([], []),
        ([1, 2], [1, 2]),
        ({}, {}),
        ({'a': 1}, {'a': 1}),
        (set(), set()),
        (set([1, 2]), set([1, 2])),
        (None, None),
    ]

    for a, b in test_cases:
        print(f"strict_equals({a}, {b}) = {strict_equals(a, b)}")