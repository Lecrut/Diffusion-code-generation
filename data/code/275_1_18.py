def filter_dict_by_value(dictionary):
    def is_valid_value(value):
        return value > 10

    for key, value in dictionary.items():
        if is_valid_value(value):
            print(f"{key}: {value}")

if __name__ == '__main__':
    sample_dict = {
        'a': 5,
        'b': 12,
        'c': 8,
        'd': 15
    }
    filter_dict_by_value(sample_dict)