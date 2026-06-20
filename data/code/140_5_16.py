def validate_record(record):
    required_fields = {'id', 'name', 'status'}
    return all(field in record and record[field] is not None for field in required_fields)

if __name__ == '__main__':
    sample_record = {
        'id': 123,
        'name': 'Example',
        'status': 'active'
    }
    print(validate_record(sample_record))