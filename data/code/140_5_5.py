def has_required_keys(data):
    required_keys = {'id', 'name', 'status'}
    return required_keys <= data.keys() and all(value is not None for value in data.values())

if __name__ == '__main__':
    sample_data = {
        'id': 123,
        'name': 'Example',
        'status': 'active'
    }
    print(has_required_keys(sample_data))