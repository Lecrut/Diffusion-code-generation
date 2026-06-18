def check_key_value(data: dict, key) -> bool:
    return key in data and data[key] is not None
if __name__ == '__main__':
    sample_data = {
        "username": "alice",
        "age": 30,
        "email": ""
    }
    requested_key = "username"
    if check_key_value(sample_data, requested_key):
        print(f"{requested_key} is present and has a valid value.")
    else:
        print(f"{requested_key} is missing or invalid.")