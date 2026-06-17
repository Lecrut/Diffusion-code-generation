def get_value(data: dict, key) -> any:
    return data.get(key) if isinstance(key, str) else None
if __name__ == '__main__':
    sample_data = {
        "user_id": 12345,
        "username": "alice",
        "role": "admin"
    }
    keys_to_check = ["user_id", "nonexistent_key", "email"]
    for key in keys_to_check:
        value = get_value(sample_data, key)
        print(f"{key}: {value}")