def map_to_simple_values(data, mapping):
    result = {}
    for key, value in mapping.items():
        if key in data:
            result[key] = data[key]
        else:
            result[key] = f"Error: Missing value for key '{key}'"
    return result
if __name__ == '__main__':
    sample_data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3
    }
    mapping_keys = ["apple", "banana", "grape"]
    result = map_to_simple_values(sample_data, {
        "apple": "fruit",
        "banana": "fruit",
        "grape": "fruit"
    })
    print(result)