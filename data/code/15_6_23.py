def check_keys_identical_values(input_dict, key1, key2):
    return {key: input_dict[key] for key in input_dict if key == key1 or key == key2}

if __name__ == '__main__':
    sample_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 2
    }
    result = check_keys_identical_values(sample_dict, 'b', 'd')
    print(result)