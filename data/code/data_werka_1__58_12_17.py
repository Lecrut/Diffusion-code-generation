def safe_first_element(iterable):
    try:
        return next(iter(iterable))
    except TypeError:
        return None

if __name__ == '__main__':
    sample_values = [
        [1, 2, 3],
        (4, 5, 6),
        "hello",
        {'a': 1, 'b': 2},
        {7, 8, 9},
        [],
        10
    ]
    for value in sample_values:
        print(safe_first_element(value))