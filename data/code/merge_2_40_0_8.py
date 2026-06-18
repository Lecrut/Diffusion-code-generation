def check_key_exists(dictionary: dict, key) -> bool:
    return key in dictionary
if __name__ == '__main__':
    data = {'apple': 1, 'banana': 2, 'cherry': 3}
    test_cases = [
        ('apple', True),
        ('date', False),
        ('banana', True)
    ]
    for key, expected in test_cases:
        result = check_key_exists(data, key)
        assert result == expected
    print("All checks passed.")