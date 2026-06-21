def get_nested_value(data, path, default=None):
    current = data
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current

if __name__ == '__main__':
    sample_data = {
        "user": {
            "profile": {
                "name": "Alice",
                "contact": {
                    "email": "alice@example.com",
                    "phone": "555-0199"
                }
            }
        },
        "status": "active"
    }
    
    path1 = ["user", "profile", "contact", "email"]
    path2 = ["user", "profile", "location"]
    path3 = ["status"]
    
    result1 = get_nested_value(sample_data, path1)
    result2 = get_nested_value(sample_data, path2, "Unknown Location")
    result3 = get_nested_value(sample_data, path3)
    
    print(result1)
    print(result2)
    print(result3)