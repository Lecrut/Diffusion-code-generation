def repeat_dictionary_keys(input_dict):
    result = []
    for _ in range(5):
        for key in input_dict:
            result.append(key)
    return result

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    repeated_keys = repeat_dictionary_keys(sample_dict)
    print(repeated_keys)