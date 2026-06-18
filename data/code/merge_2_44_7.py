def get_nested_value(data, *keys):
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
                "details": {"age": 25, "city": "NYC"}
            }
        },
        "settings": {}
    }
    result1 = get_nested_value(sample_data, "user", "profile")
    if isinstance(result1, dict):
        age = result1.get("details").get("age", None)
    result2 = sample_data.get("nonexistent_key", {}).get("nested", "default_fallback")
    print(f"Age: {age}")
    print(f"Non-existent nested value: {result2}")