def check_key_value(data: dict, key) -> bool:
    return key in data and isinstance(data[key], type(None)) is False
if __name__ == '__main__':
    sample_data = {
        'username': 'alice',
        'age': None,
        'email': ''
    }
    keys_to_check = ['username', 'missing_key']
    for k in keys_to_check:
        has_valid_value = check_key_value(sample_data, k)
        print(f"Key '{k}': {'Has valid value' if has_valid_value else 'Missing or None'}")