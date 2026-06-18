def contains_key(data: dict, key) -> bool:
    if isinstance(data, dict):
        return any(contains_key(value, key) for value in data.values())
    elif isinstance(data, list):
        return any(contains_key(item, key) for item in data)
    else:
        return False
if __name__ == '__main__':
    sample_data = {
        'a': 1,
        'b': {'c': [2, {'d': None}], 'e': [{'f': True}]},
        'g': 'h'
    }
    test_keys = ['a', 'nonexistent', 'x']
    for k in test_keys:
        result = contains_key(sample_data, k)
        print(f"Key '{k}' present: {result}")