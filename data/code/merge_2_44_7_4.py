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
                "age": 30,
                "address": {"city": "New York", "zip": "10001"}
            }
        },
        "settings": {}
    }
    age = get_nested_value(sample_data, "user", "profile", "age") or 25
    city_zip_pair = None
    if isinstance(get_nested_value(sample_data, "user", "profile"), dict):
        address_dict = get_nested_value(sample_data, "user", "profile", "address")
        if isinstance(address_dict, dict):
            city = address_dict.get("city", "Unknown City")
            zip_code = address_dict.get("zip", "00000")
            city_zip_pair = f"{city}-{zip_code}"
    print(f"Age: {age}")
    print(f"Location: {city_zip_pair}")