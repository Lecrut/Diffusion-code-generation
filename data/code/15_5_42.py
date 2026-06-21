def check_keys_identical(input_dict, key1, key2):
    return {key: value for key, value in input_dict.items() if key == key1 or key == key2}

if __name__ == '__main__':
    sample_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 2
    }
    key1 = 'b'
    key2 = 'd'
    result = check_keys_identical(sample_dict, key1, key2)
    print(result)