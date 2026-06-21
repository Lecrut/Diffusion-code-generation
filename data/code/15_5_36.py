IDENTICAL_KEYS = {'a': 'b', 'c': 'd'}

def check_identical_keys(input_dict):
    return {key: input_dict[key] == input_dict.get(value) for key, value in IDENTICAL_KEYS.items()}

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 30}
    result = check_identical_keys(sample_dict)
    print(result)