def check_keys_identical_values(input_dict, key1, key2):
    return {key: value for key, value in input_dict.items() if key == key1 or key == key2} == {key1: input_dict.get(key1), key2: input_dict.get(key2)}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result = check_keys_identical_values(sample_dict, 'a', 'b')
    print(result)