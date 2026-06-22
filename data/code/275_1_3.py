def filter_dict_by_value(dictionary):
    for key, value in dictionary.items():
        if value > 10:
            print(f"{key}: {value}")

if __name__ == '__main__':
    sample_dict = {
        'a': 5,
        'b': 12,
        'c': 8,
        'd': 15
    }
    filter_dict_by_value(sample_dict)