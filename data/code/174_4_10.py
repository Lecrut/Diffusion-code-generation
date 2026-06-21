def filter_dict_by_value(dictionary, threshold):
    return {key: value for key, value in dictionary.items() if value > threshold}

if __name__ == '__main__':
    sample_dict = {'x': 100, 'y': 200, 'z': 50, 'w': 300}
    threshold_value = 150
    filtered_dict = filter_dict_by_value(sample_dict, threshold_value)
    print(filtered_dict)