def get_nested_value(data, keys, default=None):
    current = data
    for key in keys:
        if not isinstance(current, dict):
            return default
        if key not in current:
            return default
        current = current[key]
    return current

if __name__ == '__main__':
    sample_data = {
        "user": {
            "profile": {
                "address": {
                    "city": "Springfield"
                }
            }
        },
        "config": {
            "enabled": True
        }
    }
    result = get_nested_value(sample_data, ["user", "profile", "address", "city"], "Unknown City")
    print(result)
    missing_result = get_nested_value(sample_data, ["user", "profile", "address", "zip"], "N/A")
    print(missing_result)
    invalid_path_result = get_nested_value(sample_data, ["user", "name"], "Default User")
    print(invalid_path_result)