def validate_dict(data):
    required_keys = {'id', 'name', 'status'}
    if not all(key in data for key in required_keys):
        return False
    for key in required_keys:
        if data[key] is None:
            return False
    return True

if __name__ == '__main__':
    sample_data = {
        'id': 123,
        'name': 'Example',
        'status': 'active'
    }
    print(validate_dict(sample_data))