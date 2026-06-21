THRESHOLD = 15

def filter_dict_by_value(dictionary):
    return {key: value for key, value in dictionary.items() if value > THRESHOLD}

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 30}
    filtered_dict = filter_dict_by_value(sample_dict)
    print(filtered_dict)