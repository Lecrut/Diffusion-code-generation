def get_nested_value(data, keys, default=None):
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
                "level3": "found_value"
            }
        }
    }

    result1 = get_nested_value(sample_data, ["level1", "level2", "level3"])
    print(result1)

    result2 = get_nested_value(sample_data, ["level1", "nonexistent", "level3"])
    print(result2)

    result3 = get_nested_value(sample_data, ["level1", "level2", "level3", "extra"], default="fallback")
    print(result3)

    result4 = get_nested_value({}, ["key"])
    print(result4)