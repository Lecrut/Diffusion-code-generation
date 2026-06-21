def map_keys_to_values(keys, key_value_dict):
    return {key: key_value_dict.get(key, 0) for key in keys}

if __name__ == '__main__':
    sample_keys = ["color", "size", "weight"]
    sample_dict = {
        "color": "blue",
        "size": "large"
    }
    mapped_values = map_keys_to_values(sample_keys, sample_dict)
    print(mapped_values)