def safe_first_element(iterable):
    try:
        iterator = iter(iterable)
        return next(iterator)
    except (TypeError, StopIteration):
        return None

if __name__ == '__main__':
    sample_values = [
        [10, 20, 30],
        ('a', 'b', 'c'),
        "hello",
        {'x': 1, 'y': 2},
        {1, 2, 3},
        []
    ]
    
    for value in sample_values:
        print(safe_first_element(value))