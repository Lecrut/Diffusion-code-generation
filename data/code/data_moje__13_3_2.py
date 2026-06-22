def get_nested_value(data, path):
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict):
            if key in current:
                current = current[key]
            else:
                raise KeyError(f"Key '{key}' not found in data")
        elif isinstance(current, list):
            try:
                index = int(key)
                current = current[index]
            except (ValueError, IndexError):
                raise IndexError(f"Invalid index '{key}' for list")
        else:
            raise TypeError(f"Cannot access key '{key}' on non-container type {type(current).__name__}")
    return current

if __name__ == '__main__':
    sample_data = {
        "user": {
            "name": "Alice",
            "address": {
                "city": "Wonderland",
                "zip": "12345"
            },
            "hobbies": ["reading", "gaming", "coding"]
        },
        "settings": {
            "theme": "dark",
            "notifications": True
        }
    }
    print(get_nested_value(sample_data, "user.name"))
    print(get_nested_value(sample_data, "user.address.city"))
    print(get_nested_value(sample_data, "user.hobbies.2"))
    print(get_nested_value(sample_data, "settings.theme"))