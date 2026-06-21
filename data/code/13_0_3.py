def get_nested_value(data, keys, default=None):
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

if __name__ == '__main__':
    sample_data = {
        "users": {
            "alice": {"age": 30, "city": "New York"},
            "bob": {"age": 25, "city": "London"}
        },
        "config": {
            "debug": True
        }
    }
    keys_a = ["users", "alice", "age"]
    keys_b = ["users", "charlie", "age"]
    keys_c = ["config", "debug"]
    keys_d = ["nonexistent", "path"]

    print(get_nested_value(sample_data, keys_a, default="Not Found"))
    print(get_nested_value(sample_data, keys_b, default="Not Found"))
    print(get_nested_value(sample_data, keys_c, default=False))
    print(get_nested_value(sample_data, keys_d, default="Missing Key"))