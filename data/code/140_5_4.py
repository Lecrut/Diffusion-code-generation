def validate_dictionary(data):
    required_keys = {'id', 'name', 'status'}
    return all(key in data and data[key] is not None for key in required_keys)

if __name__ == '__main__':
    sample_data = {
        'id': 456,
        'name': 'Test',
        'status': 'inactive'
    }
    result = validate_dictionary(sample_data)
    print(result)