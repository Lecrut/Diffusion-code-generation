def safe_key_check(data_dict: dict, key) -> bool:
    try:
        return isinstance(key, (str, int)) and key in data_dict
    except TypeError:
        return False
if __name__ == '__main__':
    sample_data = {
        "apple": 10,
        "banana": 20,
        3.14: None
    }
    test_keys = [
        ("orange", True),
        (5, False),
        ([], False),
        ('grape', False)
    ]
    for key, expected in test_keys:
        result = safe_key_check(sample_data, key)
        if result != expected:
            print(f"Error with key {key}: Expected {expected}, got {result}")