def validate_data(data):
    if isinstance(data, dict):
        return all(validate_data(v) for v in data.values())
    elif isinstance(data, list):
        return all(validate_data(v) for v in data)
    elif isinstance(data, str):
        return len(data) > 0 and data.isalpha()
    else:
        return False

if __name__ == '__main__':
    sample_data = {
        'a': 'hello',
        'b': ['world', {'c': 'python'}],
        'd': []
    }
    print(validate_data(sample_data))