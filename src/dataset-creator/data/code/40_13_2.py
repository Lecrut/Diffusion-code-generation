def contains_key(data: dict, key) -> bool:
    return any(key == k for sub_dict in data.values() for k in (sub_dict.keys() if isinstance(sub_dict, dict) else []))
if __name__ == '__main__':
    sample_data = {
        "user": {"id": 123},
        "settings": {"theme": "dark"},
        "metadata": {}
    }
    test_keys = ["user", "nonexistent", "settings.theme"]
    for key in test_keys:
        result = contains_key(sample_data, key)
        print(f"Key '{key}' found: {result}")