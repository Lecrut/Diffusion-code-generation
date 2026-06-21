def map_keys_to_values(keys):
    key_value_map = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4,
        "elderberry": 5
    }
    return [key_value_map.get(key, 0) for key in keys]

if __name__ == '__main__':
    sample_keys = ["apple", "banana", "fig", "grape"]
    print(map_keys_to_values(sample_keys))