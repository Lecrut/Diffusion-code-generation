def filter_dict_by_value(dictionary):
    result = {}
    for key, value in dictionary.items():
        if value > 10:
            result[key] = value
    return result

if __name__ == '__main__':
    sample_dict = {
        'a': 5,
        'b': 12,
        'c': 8,
        'd': 15
    }
    large_values = filter_dict_by_value(sample_dict)
    for key, value in large_values.items():
        print(f"{key}: {value}")