def get_nested_value(data, path):
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict):
            if key in current:
                current = current[key]
            else:
                raise KeyError(f"Key '{key}' not found in path '{path}'")
        elif isinstance(current, list):
            try:
                index = int(key)
                current = current[index]
            except ValueError:
                raise KeyError(f"Key '{key}' is not a valid index for list")
        else:
            raise TypeError(f"Cannot traverse into {type(current)}")
    return current

if __name__ == '__main__':
    sample_data = {
        "user": {
            "profile": {
                "name": "Alice",
                "age": 30,
                "settings": {
                    "theme": "dark"
                }
            },
            "orders": [
                {"id": 1, "status": "shipped"},
                {"id": 2, "status": "pending"}
            ]
        }
    }
    
    path1 = "user.profile.name"
    result1 = get_nested_value(sample_data, path1)
    print(result1)
    
    path2 = "user.orders.1.status"
    result2 = get_nested_value(sample_data, path2)
    print(result2)
    
    path3 = "user.profile.settings.theme"
    result3 = get_nested_value(sample_data, path3)
    print(result3)