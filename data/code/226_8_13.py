def repeat_keys(dictionary):
    result = []
    for _ in range(5):
        result.extend(list(dictionary.keys()))
    return result

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    repeated_keys = repeat_keys(sample_dict)
    print(repeated_keys)