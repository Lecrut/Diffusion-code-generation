def validate_dict(data):
    required_keys = {'id', 'name', 'status'}
    if not isinstance(data, dict):
        return False
    return all(key in data and data[key] is not None for key in required_keys)

if __name__ == '__main__':
    sample_data = {
        'id': 123,
        'name': 'Example',
        'status': 'active'
    }
    print(validate_dict(sample_data))