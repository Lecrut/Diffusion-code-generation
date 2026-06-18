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
            },
            "settings": None
        }
    }
    age = get_nested_value(sample_data, "user", "profile", "age")
    city = get_nested_value(sample_data, "user", "profile", "address", "city")
    zip_code = get_nested_value(sample_data, "user", "profile", "address", "zip")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Zip Code: {zip_code}")