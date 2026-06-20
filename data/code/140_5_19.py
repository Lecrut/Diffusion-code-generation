REQUIRED_KEYS = {'id', 'name', 'status'}

def validate_dict(data):
    return all(key in data and data[key] is not None for key in REQUIRED_KEYS)

if __name__ == '__main__':
    sample_data = {
        'id': 123,
        'name': 'Example',
        'status': 'active'
    }
    print(validate_dict(sample_data))