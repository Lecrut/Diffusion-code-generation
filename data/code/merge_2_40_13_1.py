def safe_key_check(data: dict, keys) -> bool:
    for key in keys:
        try:
            _ = data[key]
            return True
        except KeyError:
            continue
    return False
if __name__ == '__main__':
    sample_data = {
        "user": {"id": 123, "details": {"active": True}},
        "settings": {"theme": "dark", "notifications": False}
    }
    test_keys_1 = ["user"]
    result_1 = safe_key_check(sample_data, test_keys_1)
    test_keys_2 = ["nonexistent"]
    result_2 = safe_key_check(sample_data, test_keys_2)
    print(f"Key '{test_keys_1[0]}' found: {result_1}")
    print(f"Key '{test_keys_2[0]}' found: {result_2}")