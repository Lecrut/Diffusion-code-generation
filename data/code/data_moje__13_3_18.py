def get_nested_value(data, path):
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict):
            if key in current:
                current = current[key]
            else:
                raise KeyError(key)
        elif isinstance(current, list):
            try:
                index = int(key)
                current = current[index]
            except (ValueError, IndexError):
                raise IndexError(f"Invalid index '{key}'")
        else:
            raise AttributeError(f"'{type(current).__name__}' object has no attribute '{key}'")
    return current

if __name__ == '__main__':
    sample_data = {
        "user": {
            "address": {
                "city": "New York"
            }
        },
        "items": [1, 2, {"id": 101, "name": "Widget"}]
    }

    print(get_nested_value(sample_data, "user.address.city"))
    print(get_nested_value(sample_data, "items.2.name"))