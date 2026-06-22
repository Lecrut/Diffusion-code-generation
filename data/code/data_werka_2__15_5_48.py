def check_keys_identical(input_dict, key1, key2):
    value1 = input_dict.get(key1)
    value2 = input_dict.get(key2)
    return {key1: value1 == value2}

if __name__ == '__main__':
    sample_dict = {'first': 9, 'second': 3, 'third': 9}
    result = check_keys_identical(sample_dict, 'first', 'third')
    print(result)