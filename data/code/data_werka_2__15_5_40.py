def check_keys_identical_values(input_dict, key1, key2):
    return {key1: input_dict[key1] == input_dict.get(key2)}

if __name__ == '__main__':
    sample_dict = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    result = check_keys_identical_values(sample_dict, 'a', 'b')
    print(result)