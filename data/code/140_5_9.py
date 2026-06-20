def validate_dict(data):
    required_keys = {'id', 'name', 'status'}
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    if not required_keys.issubset(data):
        missing_keys = required_keys - data.keys()
        raise KeyError(f"Missing keys: {missing_keys}")
    for key in required_keys:
        if data[key] is None:
            raise ValueError(f"Value for '{key}' cannot be None")
    return True

if __name__ == '__main__':
    sample_data = {
        'id': 123,
        'name': 'Example',
        'status': 'active'
    }
    try:
        print(validate_dict(sample_data))
    except (ValueError, KeyError) as e:
        print(e)