def safe_first_element(iterable):
    try:
        return next(iter(iterable))
    except (TypeError, StopIteration):
        return None

if __name__ == '__main__':
    sample_values = {
        'list': [10, 20, 30],
        'tuple': (40, 50, 60),
        'string': "hello",
        'dict': {'key1': 'value1', 'key2': 'value2'},
        'set': {70, 80, 90},
        'empty_list': []
    }
    
    for category, value in sample_values.items():
        print(f"First element of {category}: {safe_first_element(value)}")