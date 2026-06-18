def get_value(data: dict, key) -> any:
    return data.get(key)
if __name__ == '__main__':
    sample_data = {
        "user_id": 1001,
        "username": "alice",
        "email": "alice@example.com"
    }
    print(get_value(sample_data, "user_id"))