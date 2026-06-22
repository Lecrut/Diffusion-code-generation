def repeat_dictionary_keys(dictionary, count):
    result = []
    for _ in range(count):
        result.extend(dictionary.keys())
    return result

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    repetition_count = 5
    repeated_keys = repeat_dictionary_keys(sample_dict, repetition_count)
    print(repeated_keys)