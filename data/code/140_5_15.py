def validate_required_keys(data):
    required_keys = {'id', 'name', 'status'}
    return all(key in data and data[key] is not None for key in required_keys)

if __name__ == '__main__':
    sample_data = {
        'id': 123,
        'name': 'Example',
        'status': 'active'
    }
    print(validate_required_keys(sample_data))