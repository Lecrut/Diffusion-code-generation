def safe_first_element(iterable):
    try:
        return next(iter(iterable))
    except TypeError:
        return None

if __name__ == '__main__':
    sample_values = {
        'list': [1, 2, 3],
        'tuple': (4, 5, 6),
        'string': "hello",
        'dict': {'a': 1, 'b': 2},
        'set': {7, 8, 9},
        'empty_list': []
    }
    
    for key, value in sample_values.items():
        print(f"First element of {key}: {safe_first_element(value)}")