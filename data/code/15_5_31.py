def check_keys_identical(input_dict, key1, key2):
    return {key1: input_dict[key1] == input_dict.get(key2)}

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 10}
    result = check_keys_identical(sample_dict, 'a', 'c')
    print(result)