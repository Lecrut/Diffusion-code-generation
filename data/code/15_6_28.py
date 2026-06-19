def check_keys_identical(input_dict, key1, key2):
    return {key: input_dict[key] for key in input_dict if input_dict.get(key1) == input_dict.get(key2)}

if __name__ == '__main__':
    sample_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 2
    }
    result = check_keys_identical(sample_dict, 'b', 'd')
    print(result)