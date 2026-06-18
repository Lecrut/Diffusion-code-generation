def check_key_exists(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    sample_dict = {'apple': 10, 'banana': 20, 'cherry': 30}
    test_cases = [
        ('apple', True),
        ('grape', False),
        (None, None in sample_dict) if isinstance(sample_dict.get('null'), type(None)) else ('null_key', False)
    ]
    for key, expected_result in test_cases:
        result = check_key_exists(sample_dict, key)
        assert result == expected_result, f"Failed for key {key}"
    print("All checks passed.")