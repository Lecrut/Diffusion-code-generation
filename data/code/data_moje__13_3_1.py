def get_nested_value(data, path, default=None):
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

if __name__ == '__main__':
    sample_data = {
        "level1": {
            "level2": {
                "level3": {
                    "value": 42
                }
            }
        }
    }
    result = get_nested_value(sample_data, "level1.level2.level3.value")
    print(result)