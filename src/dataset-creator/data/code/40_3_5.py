def safe_key_check(data: dict, key) -> bool:
    try:
        return isinstance(key, (str, int)) and key in data.keys()
    except TypeError:
        return False
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20}
    test_cases = [
        ('apple', True),
        ('orange', False),
        (3.5, False),
        ([], False)
    ]
    for key, expected in test_cases:
        result = safe_key_check(sample_data, key)
        assert result == expected, f"Failed for key {key}"
    print("All tests passed.")