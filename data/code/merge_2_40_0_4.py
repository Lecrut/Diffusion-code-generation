def check_key_exists(data_dict: dict, target_key) -> bool:
    return target_key in data_dict
if __name__ == '__main__':
    sample_data = {"apple": 10, "banana": 20, "cherry": 30}
    test_keys = ["orange", "banana"]
    for key in test_keys:
        result = check_key_exists(sample_data, key)
        print(f"Key '{key}' exists: {result}")