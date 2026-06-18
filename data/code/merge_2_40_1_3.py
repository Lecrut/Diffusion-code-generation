def contains_key(data: dict, key) -> bool:
    if not isinstance(data, dict):
        return False
    for k in data.keys():
        if k == key:
            return True
        value = data[k]
        if isinstance(value, (dict, list)):
            if contains_key(value, key):
                return True
    return False
if __name__ == '__main__':
    sample_dict = {
        'a': 1,
        'b': {'c': 2},
        'd': [3, {'e': 4}]
    }
    test_keys = ['a', 'nonexistent']
    for k in test_keys:
        result = contains_key(sample_dict, k)
        print(f"Key '{k}' found: {result}")