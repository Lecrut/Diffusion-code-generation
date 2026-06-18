def verify_key_in_dict(data: dict, target) -> bool:
    try:
        return target in data.keys()
    except TypeError:
        return False
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20}
    test_cases = [
        ('apple', True),
        (5, False),
        ({'nested': 'dict'}, False)
    ]
    for item, expected in test_cases:
        result = verify_key_in_dict(sample_data, item)
        assert result == expected, f"Test failed for {item}"