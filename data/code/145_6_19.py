def validate_data(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if not (isinstance(key, str) and isinstance(value, bool)):
                return False
            if not validate_data(value):
                return False
    elif isinstance(data, list):
        for item in data:
            if not validate_data(item):
                return False
    else:
        return False
    return True

if __name__ == '__main__':
    sample_data = {
        'a': True,
        'b': {
            'c': False,
            'd': [True, False]
        },
        'e': []
    }
    print(validate_data(sample_data))