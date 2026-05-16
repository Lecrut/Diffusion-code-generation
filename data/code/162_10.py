def process_map_data(data_dict):
    result_dict = {}
    for map_name, value in data_dict.items():
        result_dict[map_name] = value
    return result_dict
if __name__ == '__main__':
    sample_data = {
        "map_a": "value_a",
        "map_b": "value_b",
        "map_c": "value_c"
    }
    processed_data = process_map_data(sample_data)
    print(processed_data)