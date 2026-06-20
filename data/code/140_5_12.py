def validate_record(record):
    required_keys = {'id', 'name', 'status'}
    return all(key in record and record[key] is not None for key in required_keys)

if __name__ == '__main__':
    sample_record = {
        'id': 123,
        'name': 'Example',
        'status': 'active'
    }
    print(validate_record(sample_record))