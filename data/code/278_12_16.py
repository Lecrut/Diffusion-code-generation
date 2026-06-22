KEY_VALUE_FORMAT = "Key: {}, Value: {}"

def print_dict_pairs(dictionary):
    for key, value in dictionary.items():
        print(KEY_VALUE_FORMAT.format(key, value))

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print_dict_pairs(sample_dict)