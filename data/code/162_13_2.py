def filter_dictionary(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        output_dict[key] = value
    return output_dict
if __name__ == '__main__':
    sample_dict = {"a": 1, "b": 2, "c": 3}
    result = filter_dictionary(sample_dict)
    print(result)