def repeat_and_merge_dict(input_dict, repetitions):
    result = {}
    for key, value in input_dict.items():
        result[key] = [value] * repetitions
    return result

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2}
    repetitions = 3
    repeated_and_merged = repeat_and_merge_dict(sample_dict, repetitions)
    print(repeated_and_merged)