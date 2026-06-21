def get_nested_value(data, path, default=None):
    current = data
    for key in path:
        try:
            if isinstance(current, dict):
                current = current[key]
            else:
                return default
        except (KeyError, TypeError, IndexError):
            return default
    return current

if __name__ == '__main__':
    sample_data = {
        "user": {
            "profile": {
                "name": "Alice",
                "settings": {
                    "theme": "dark"
                }
            }
        }
    }
    
    path_1 = ["user", "profile", "name"]
    result_1 = get_nested_value(sample_data, path_1, "Guest")
    print(result_1)
    
    path_2 = ["user", "profile", "email"]
    result_2 = get_nested_value(sample_data, path_2, "Not Found")
    print(result_2)
    
    path_3 = ["user", "settings", "theme"]
    result_3 = get_nested_value(sample_data, path_3, "default_theme")
    print(result_3)
    
    path_4 = []
    result_4 = get_nested_value(sample_data, path_4, None)
    print(result_4)