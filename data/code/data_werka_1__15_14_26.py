def strict_equal(value1, value2):
    return type(value1) is type(value2) and value1 == value2

if __name__ == '__main__':
    test_cases = [
        (5, 5),
        (5.0, 5),
        ('hello', 'hello'),
        ([], []),
        ({}, {}),
        (None, None),
        (True, False),
        (12345678901234567890, 12345678901234567890),
    ]

    for value1, value2 in test_cases:
        print(strict_equal(value1, value2))