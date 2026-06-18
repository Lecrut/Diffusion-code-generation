def is_key_present(data_dict: dict, key_to_check) -> bool:
    return key in data_dict
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 25, 'cherry': 3.7}
    test_cases = [
        ('apple', True),
        ('grape', False),
        (None, False)
    ]
    for key, expected in test_cases:
        result = is_key_present(sample_data, key)
        print(f"Key '{key}' present? {result} (Expected: {expected})")