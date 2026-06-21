def filter_dict_by_value(d, threshold):
    return {k: v for k, v in d.items() if v >= threshold}

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 3}
    threshold = 10
    filtered_dict = filter_dict_by_value(sample_dict, threshold)
    print(filtered_dict)