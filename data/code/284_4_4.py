def reverse_dict_keys(input_dict):
    return {key: input_dict[key] for key in reversed(list(input_dict.keys()))}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print(reverse_dict_keys(sample_dict))