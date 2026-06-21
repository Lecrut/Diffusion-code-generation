def filter_dict_by_value(dictionary, threshold):
    return {key: value for key, value in dictionary.items() if value > threshold}

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 30}
    threshold_value = 15
    filtered_dict = filter_dict_by_value(sample_dict, threshold_value)
    print(filtered_dict)