def check_key_value(data: dict, key) -> bool:
    return key in data and data[key] is not None
if __name__ == '__main__':
    sample_data = {
        "username": "alice",
        "email": "",
        "age": 30,
        "role": None
    }
    target_key = "email"
    if check_key_value(sample_data, target_key):
        print(f"{target_key} is assigned a value.")
    else:
        print(f"{target_key} has no valid assignment or does not exist.")