def safe_first_element(iterable):
    try:
        iterator = iter(iterable)
        return next(iterator)
    except (TypeError, StopIteration):
        return None

if __name__ == '__main__':
    sample_values = {
        'list': [1, 2, 3],
        'tuple': (4, 5, 6),
        'string': "hello",
        'dict': {'a': 1, 'b': 2},
        'set': {7, 8, 9},
        'empty_list': [],
        'range': range(5),
        'generator': (x for x in [10, 20, 30])
    }
    
    for key, value in sample_values.items():
        first_element = safe_first_element(value)
        print(f"First element of {key}: {first_element}")