def efficient_mapping(input_dict, mapping_rule):
    output_dict = {}
    for key, value in input_dict.items():
        new_key = mapping_rule(key)
        output_dict[new_key] = value
    return output_dict
if __name__ == '__main__':
    input_data = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }
    def simple_prefix_mapping(key):
        return "prefix_" + key
    mapping_function = simple_prefix_mapping
    result = efficient_mapping(input_data, mapping_function)
    print(result)