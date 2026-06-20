def validate_dict(data):
    required_keys = {'id', 'name', 'status'}
    return all((key in data and data[key] is not None for key in required_keys))
if __name__ == '__main__':
    sample_data = {'id': 123, 'name': 'Example', 'status': 'active'}
    print(validate_dict(sample_data))
    sample_data_missing_key = {'id': 123, 'name': 'Example'}
    print(validate_dict(sample_data_missing_key))
    sample_data_none_value = {'id': None, 'name': 'Example', 'status': 'active'}
    print(validate_dict(sample_data_none_value))