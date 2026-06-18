def check_key_value(data: dict, key) -> bool:
    return key in data and data[key] is not None
if __name__ == '__main__':
    sample_data = {
        "username": "alice",
        "age": 30,
        "email": "",
        "role": None
    }
    keys_to_check = ["username", "missing_key"]
    for k in keys_to_check:
        result = check_key_value(sample_data, k)
        print(f"Key '{k}' has a valid value: {result}")