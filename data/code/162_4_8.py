def map_values_safely(data_map, required_keys):
    result = {}
    for key in required_keys:
        if key in data_map:
            result[key] = data_map[key]
        else:
            result[key] = f"Error: Missing key '{key}'"
    return result
if __name__ == '__main__':
    sample_data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3
    }
    required = ["apple", "banana", "date"]
    output = map_values_safely(sample_data, required)
    print(output)