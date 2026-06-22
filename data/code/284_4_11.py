def reverse_dict_keys(input_dict):
    return {key: value for key, value in reversed(list(input_dict.items()))}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print(reverse_dict_keys(sample_dict))