def get_value(data: dict, key) -> any:
    return data.get(key)
if __name__ == '__main__':
    sample_data = {
        "user_id": 1001,
        "username": "alice",
        "active": True,
        "score": 95.5
    }
    keys_to_check = ["user_id", "nonexistent_key", "active"]
    for k in keys_to_check:
        print(f"Key {k}: ", end="")
        result = get_value(sample_data, k)
        if isinstance(result, bool):
            print(str(result).lower())
        else:
            print(repr(result))