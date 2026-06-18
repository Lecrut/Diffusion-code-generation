def safe_key_check(data: dict, key) -> bool:
    try:
        return isinstance(key, (str, int, float)) and key in data
    except TypeError:
        return False
if __name__ == '__main__':
    sample_data = {'apple': 50, 'banana': 20}
    test_cases = [
        ('apple', True),
        ('orange', False),
        (1234567890, None),                                                                         
        ([], False)                                                          
    ]
    print(f"Checking existence of 'apple' in sample_data: {safe_key_check(sample_data, 'apple')}")
    print(f"Checking existence of 'orange' in sample_data: {safe_key_check(sample_data, 'orange')}")