def check_key_value(data: dict, key) -> bool:
    return key in data and data[key] is not None
if __name__ == '__main__':
    sample_data = {"apple": "red", "banana": None, "cherry": 5}
    test_cases = [
        ("apple", True),
        ("banana", False),
        ("grape", False),
        (None, False)
    ]
    for key, expected in test_cases:
        result = check_key_value(sample_data, key)
        assert result == expected, f"Test failed for key {key}"
    print("All checks passed.")