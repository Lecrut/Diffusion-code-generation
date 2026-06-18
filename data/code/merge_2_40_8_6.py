def check_key_value(data: dict, key) -> bool:
    return key in data and data[key] is not None
if __name__ == '__main__':
    sample_data = {
        "username": "alice",
        "age": 30,
        "email": "",
        "city": None
    }
    keys_to_check = ["username", "nonexistent_key", "email"]
    for k in keys_to_check:
        result = check_key_value(sample_data, k)
        print(f"Key '{k}': {'Has value' if result else 'No valid value'}")