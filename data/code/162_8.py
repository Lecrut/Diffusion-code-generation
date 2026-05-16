def efficient_mapping(input_dict, mapping_rule):
    result_dict = {}
    for key, value in input_dict.items():
        new_key = mapping_rule(key)
        result_dict[new_key] = value
    return result_dict
if __name__ == '__main__':
    input_data = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }
    mapping_function = lambda x: x.upper()
    output_data = efficient_mapping(input_data, mapping_function)
    print(output_data)