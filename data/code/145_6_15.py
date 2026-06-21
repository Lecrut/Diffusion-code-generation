def validate_data(data):
    if isinstance(data, dict):
        return all(validate_data(value) for value in data.values())
    elif isinstance(data, list):
        return all(validate_data(item) for item in data)
    elif isinstance(data, bool):
        return True
    else:
        return False

if __name__ == '__main__':
    sample_data = {
        'a': True,
        'b': [False, {'c': True}],
        'd': [{'e': False}, {'f': [True, False]}]
    }
    print(validate_data(sample_data))