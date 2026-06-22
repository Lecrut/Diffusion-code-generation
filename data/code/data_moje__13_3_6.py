def get_nested_value(data, path):
    parts = path.split('.')
    current = data
    for part in parts:
        if isinstance(current, dict):
            if part in current:
                current = current[part]
            else:
                raise KeyError(f"Key '{part}' not found")
        elif isinstance(current, list):
            try:
                index = int(part)
                current = current[index]
            except (ValueError, IndexError):
                raise KeyError(f"Index '{part}' not found or invalid")
        else:
            raise TypeError(f"Cannot access '{part}' in {type(current).__name__}")
    return current

if __name__ == '__main__':
    sample_data = {
        "level1": {
            "level2": {
                "level3": "deep_value"
            },
            "list_field": [
                "item0",
                "item1"
            ]
        }
    }
    result = get_nested_value(sample_data, "level1.level2.level3")
    print(result)
    result2 = get_nested_value(sample_data, "level1.list_field.1")
    print(result2)