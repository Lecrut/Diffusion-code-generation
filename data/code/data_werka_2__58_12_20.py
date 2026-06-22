def safe_first_element(iterable):
    if hasattr(iterable, '__iter__'):
        iterator = iter(iterable)
        return next(iterator, None)
    else:
        raise ValueError("Provided input is not an iterable")

if __name__ == '__main__':
    sample_values = [
        [1, 2, 3],
        (4, 5, 6),
        "hello",
        {'a': 1, 'b': 2},
        {7, 8, 9},
        []
    ]
    
    for value in sample_values:
        try:
            print(safe_first_element(value))
        except ValueError as e:
            print(e)