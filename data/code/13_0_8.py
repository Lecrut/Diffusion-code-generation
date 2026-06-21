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
                "age": 30
            }
        }
    }
    
    result1 = get_nested_value(sample_data, ["user", "profile", "name"])
    print(result1)
    
    result2 = get_nested_value(sample_data, ["user", "profile", "email"], default="N/A")
    print(result2)
    
    result3 = get_nested_value(sample_data, ["user", "address", "city"], default="Unknown")
    print(result3)