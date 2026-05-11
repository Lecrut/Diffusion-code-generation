def efficient_mapping(input_dict, mapping_function):
    output_dict = {}
    for key, value in input_dict.items():
        output_dict[mapping_function(key, value)] = value
    return output_dict
if __name__ == '__main__':
    sample_input = {
        "a": 10,
        "b": 20,
        "c": 30,
        "d": 40
    }
    def custom_mapper(k, v):
        return str(k) + "_" + str(v)
    result = efficient_mapping(sample_input, custom_mapper)
    print(result)