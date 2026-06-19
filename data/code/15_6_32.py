def check_keys_identical(input_dict, key1, key2):
    return {key: value for key, value in input_dict.items() if key == key1 and key2 in input_dict and input_dict[key1] == input_dict[key2]}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 1}
    result = check_keys_identical(sample_dict, 'a', 'd')
    print(result)