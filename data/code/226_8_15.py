def repeat_dict_keys(dictionary):
    return list(dictionary.keys()) * 5

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    repeated_keys = repeat_dict_keys(sample_dict)
    print(repeated_keys)