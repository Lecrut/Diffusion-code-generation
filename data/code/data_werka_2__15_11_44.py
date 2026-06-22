def check_strict_equality(a, b):
    if a is None or b is None:
        return a == b
    else:
        return a is b and a == b

if __name__ == '__main__':
    sample_values = [
        (None, None),
        (10, 10),
        ('hello', 'hello'),
        ([], []),
        ({}, {}),
        (None, 0),
        (1.5, 1.5),
        (True, True),
        (False, False),
        ((1, 2), (1, 2))
    ]

    for a, b in sample_values:
        print(check_strict_equality(a, b))