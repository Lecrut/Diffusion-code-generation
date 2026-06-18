def check_key_value(data: dict, key) -> bool:
    return key in data and data[key] is not None
if __name__ == '__main__':
    sample_data = {
        "username": "alice",
        "email": "",
        "age": 30,
        "role": None
    }
    requested_key = "email"
    if check_key_value(sample_data, requested_key):
        print(f"The key '{requested_key}' has a valid value.")
    else:
        print(f"The key '{requested_key}' is missing or assigned an empty/null value.")