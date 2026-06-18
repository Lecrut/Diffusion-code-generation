def contains_key(data: dict, key) -> bool:
    if isinstance(data, dict):
        return key in data or any(contains_key(v, key) for v in data.values())
    elif isinstance(data, list):
        return any(contains_key(item, key) for item in data)
    else:
        return False
if __name__ == '__main__':
    sample_data = {
        'a': 1,
        'b': {'c': [2, {'d': None}], 'e': True},
        'f': [{'g': 'h', 'i': ['j']}]
    }
    target_key = 'd'
    result = contains_key(sample_data, target_key)
    print(result)