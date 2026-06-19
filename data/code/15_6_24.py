def check_keys_identical(input_dict, key1, key2):
    return {key: (input_dict[key1] == input_dict[key2]) for key in input_dict if key in [key1, key2]}

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 30}
    result = check_keys_identical(sample_dict, 'a', 'b')
    print(result)