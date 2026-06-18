def check_key_value(data: dict, key) -> bool:
    return key in data and isinstance(data[key], (int, float, str, list, tuple))
if __name__ == '__main__':
    sample_data = {
        "apple": 5,
        "banana": ["red", "green"],
        "orange": None,
        "grape": "purple"
    }
    keys_to_check = ["apple", "missing_key"]
    for k in keys_to_check:
        result = check_key_value(sample_data, k)
        print(f"Key '{k}' has a valid value: {result}")