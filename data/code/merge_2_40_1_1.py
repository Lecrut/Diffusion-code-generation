def contains_key(data, key):
    if isinstance(data, dict) and key in data:
        return True
    elif isinstance(data, list):
        for item in data:
            if contains_key(item, key):
                return True
    else:
        return False
if __name__ == '__main__':
    sample_data = {
        "level1": {
            "level2": {
                "target_key": "value",
                "nested_list": [
                    {"another_nested": {"deep_key": True}},
                    42,
                    None
                ]
            },
            "other_key": "ignored"
        }
    }
    test_keys = ["target_key", "nonexistent", "level1"]
    for key in test_keys:
        result = contains_key(sample_data, key)
        print(f"Key '{key}' found: {result}")