def verify_key_in_nested_dict(data: dict, key: str) -> bool:
    if not isinstance(data, dict):
        return False
    for k in data.keys():
        if k == key:
            return True
        elif isinstance(data[k], (dict, list)):
            result = verify_key_in_nested_dict(data[k], key)
            if result:
                return True
    return False
if __name__ == '__main__':
    sample_data = {
        'user': {'id': 123, 'details': {'role': 'admin'}},
        'config': ['setting_a', 'setting_b'],
        'metadata': {}
    }
    test_key_1 = 'role'
    test_key_2 = 'nonexistent'
    test_key_3 = 'user'
    result_1 = verify_key_in_nested_dict(sample_data, test_key_1)
    result_2 = verify_key_in_nested_dict(sample_data, test_key_2)
    result_3 = verify_key_in_nested_dict(sample_data, test_key_3)
    print(f"Key '{test_key_1}' found: {result_1}")
    print(f"Key '{test_key_2}' found: {result_2}")
    print(f"Key '{test_key_3}' found: {result_3}")