def build_dynamic_mapping(data_source):
    return {item: item * 2 for item in data_source}
if __name__ == '__main__':
    sample_data = ['a', 'b', 'c']
    result_map = build_dynamic_mapping(sample_data)
    print(result_map)