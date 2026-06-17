def contains_key(data: dict, key) -> bool:
    if isinstance(data, dict):
        return key in data or any(contains_key(value, key) for value in data.values())
    elif isinstance(data, list):
        return any(contains_key(item, key) for item in data)
    else:
        return False
if __name__ == '__main__':
    sample_data = {
        'a': 1,
        'b': {'c': [2, {'d': 3}, None], 'e': True}
    }
    target_key = 'd'
    result = contains_key(sample_data, target_key)
    print(result if isinstance(result, bool) else "Error")