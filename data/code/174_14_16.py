def filter_dict_by_value(input_dict, threshold):
    return {key: value for key, value in input_dict.items() if value >= threshold}

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 3}
    threshold = 10
    filtered_dict = filter_dict_by_value(sample_dict, threshold)
    print(filtered_dict)