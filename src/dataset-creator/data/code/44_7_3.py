def get_nested_value(data: dict, *keys):
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current
if __name__ == '__main__':
    sample_data = {
        "user": {
            "profile": {
                "age": 30,
                "address": {"city": "New York", "zip": "10001"}
            }
        },
        "settings": {}
    }
    age = get_nested_value(sample_data, "user", "profile", "age")
    city = get_nested_value(sample_data, "user", "profile", "address", "city")
    zip_code = get_nested_value(sample_data, "user", "profile", "address", "zip")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Zip Code: {zip_code}")
    def get_with_default(data, *keys):
        current = data
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return None
        def safe_get(d, key):
            return d.get(key) if isinstance(d, dict) and key in d else None
    city_default = get_with_default(sample_data, "user", "profile", "address", "city")
    def deep_get(d, *path):
        for k in path:
            if isinstance(d, dict) and d.get(k) is not None:
                d = d[k]
            else:
                return "Key missing"
        return d
    result1 = deep_get(sample_data, "user", "profile")
    print(f"Nested object access: {result1}")
    def get_safe(d, *keys):
        val = d.get(keys[0]) if keys else None
        while isinstance(val, dict) and len(keys) > 1:
            key = keys.pop(0)
            val = val.get(key)
        return "Key missing" if val is None or not isinstance(val, (dict, list)) else val
    def get_nested_safe(data: dict, *keys):
        current = data
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current.get(key)
            else:
                return None
        return current
    print(f"Age via get_nested_safe: {get_nested_safe(sample_data, 'user', 'profile', 'age')}")
    missing_val = get_nested_safe(sample_data, "nonexistent", "key")
    print(f"Missing value result: {missing_val}")