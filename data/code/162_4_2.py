def map_to_simple_values(data_dict, mapping):
    result = {}
    for key, value in mapping.items():
        if key in data_dict:
            result[key] = data_dict[key]
        else:
            result[key] = f"Error: Missing value for key '{key}'"
    return result
if __name__ == '__main__':
    sample_data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3
    }
    mapping_to_check = {
        "apple": "fruit",
        "banana": "fruit",
        "grape": "fruit",
        "cherry": "fruit"
    }
    output = map_to_simple_values(sample_data, mapping_to_check)
    print(output)