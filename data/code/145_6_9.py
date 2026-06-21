def validate_data(data):
    if isinstance(data, dict):
        return all(validate_data(v) for v in data.values())
    elif isinstance(data, list):
        return all(validate_data(v) for v in data)
    elif isinstance(data, str):
        return len(data) > 0 and not data.isdigit()
    elif isinstance(data, int):
        return data >= 0
    else:
        return False

if __name__ == '__main__':
    sample_data = {
        'a': 1,
        'b': [2, 3],
        'c': {'d': 'hello', 'e': []},
        'f': 'world'
    }
    print(validate_data(sample_data))