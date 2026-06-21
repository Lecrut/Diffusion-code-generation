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
        "users": {
            "admin": {
                "email": "admin@example.com",
                "settings": {
                    "theme": "dark"
                }
            },
            "guest": {
                "email": "guest@example.com"
            }
        }
    }
    
    print(get_nested_value(sample_data, ["users", "admin", "email"], "default@example.com"))
    print(get_nested_value(sample_data, ["users", "admin", "settings", "theme"], "light"))
    print(get_nested_value(sample_data, ["users", "guest", "settings", "theme"], "light"))
    print(get_nested_value(sample_data, ["nonexistent", "path"], "fallback"))
    print(get_nested_value(sample_data, ["users", "admin"], {"email": "default"}))
    print(get_nested_value(sample_data, "string_path", None))
    print(get_nested_value(None, ["a"], "none_data"))
    print(get_nested_value(sample_data, [], "empty_path_result"))