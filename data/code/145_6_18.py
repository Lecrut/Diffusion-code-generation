def validate_data(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if not (isinstance(key, str) and isinstance(value, bool)):
                return False
    elif isinstance(data, list):
        for item in data:
            if not isinstance(item, bool):
                return False
    else:
        return False
    return True

if __name__ == '__main__':
    sample_data = {
        'a': True,
        'b': False,
        'c': {
            'd': True,
            'e': False
        }
    }
    print(validate_data(sample_data))