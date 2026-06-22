def are_strictly_equal(value1, value2):
    if value1 is None or value2 is None:
        return value1 is value2
    else:
        return value1 == value2

if __name__ == '__main__':
    sample_values = [
        (None, None),
        (None, 0),
        (0, 0),
        ('hello', 'hello'),
        ([], []),
        ({}, {}),
        (123456789, 123456789),
        ((1, 2), (1, 2))
    ]

    for val1, val2 in sample_values:
        result = are_strictly_equal(val1, val2)
        print(f"are_strictly_equal({val1}, {val2}) = {result}")