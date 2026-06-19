def check_keys_identical(input_dict):
    return {key: value for key, value in input_dict.items() if len(set(value)) == 1}

if __name__ == '__main__':
    sample_dict = {
        'key1': [1, 1, 1],
        'key2': [2, 2, 3],
        'key3': [4, 4, 4],
        'key4': [5, 6, 7]
    }
    result = check_keys_identical(sample_dict)
    print(result)