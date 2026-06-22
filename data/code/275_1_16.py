def filter_dict_by_value(dictionary):
    large_values = {key: value for key, value in dictionary.items() if value > 10}
    return large_values

if __name__ == '__main__':
    sample_dict = {
        'x': 7,
        'y': 20,
        'z': 14,
        'w': 9
    }
    result = filter_dict_by_value(sample_dict)
    print(result)