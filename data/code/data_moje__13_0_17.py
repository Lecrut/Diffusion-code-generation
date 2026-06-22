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
                "details": {
                    "age": 30
                }
            },
            "settings": {
                "theme": "dark"
            }
        }
    }
    
    result1 = get_nested_value(sample_data, ["user", "profile", "name"])
    print(result1)
    
    result2 = get_nested_value(sample_data, ["user", "settings", "theme"])
    print(result2)
    
    result3 = get_nested_value(sample_data, ["user", "nonexistent", "key"], default="MISSING")
    print(result3)
    
    result4 = get_nested_value(sample_data, ["user", "profile", "details", "age"])
    print(result4)