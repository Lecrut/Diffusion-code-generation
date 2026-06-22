def get_nested_value(nested_dict, path, default=None):
    result = nested_dict
    for key in path:
        if isinstance(result, dict) and key in result:
            result = result[key]
        else:
            return default
    return result

if __name__ == '__main__':
    sample_dict = {
        "level1": {
            "level2": {
                "level3": "deep_value"
            }
        },
        "list_item": [1, 2, 3]
    }

    print(get_nested_value(sample_dict, ["level1", "level2", "level3"]))
    print(get_nested_value(sample_dict, ["missing_key"], "fallback"))
    print(get_nested_value(sample_dict, ["list_item", 0]))