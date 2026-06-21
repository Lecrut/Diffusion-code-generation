def get_nested_value(data, path, default=None):
    current = data
    for key in path:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

if __name__ == '__main__':
    sample_data = {
        "user": {
            "profile": {
                "name": "Alice",
                "age": 30,
                "address": {
                    "city": "New York",
                    "zip": "10001"
                }
            },
            "active": True
        },
        "settings": {
            "theme": "dark"
        }
    }
    path1 = ["user", "profile", "address", "city"]
    path2 = ["user", "profile", "email"]
    path3 = ["user", "settings", "notifications"]
    path4 = ["user", "profile", "name"]
    result1 = get_nested_value(sample_data, path1, "Unknown")
    result2 = get_nested_value(sample_data, path2, "No email")
    result3 = get_nested_value(sample_data, path3, False)
    result4 = get_nested_value(sample_data, path4, "Default Name")
    print(result1)
    print(result2)
    print(result3)
    print(result4)