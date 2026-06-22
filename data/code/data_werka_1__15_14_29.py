def strict_equal(a, b):
    return type(a) is type(b) and a == b

if __name__ == '__main__':
    test_cases = [
        (1, 1),
        (1, '1'),
        ('1', '1'),
        (1.0, 1),
        (True, 1),
        ([], []),
        ({}, {}),
        ((1, 2), (1, 2)),
        (set(), set()),
    ]

    for a, b in test_cases:
        print(f"strict_equal({a}, {b}) = {strict_equal(a, b)}")