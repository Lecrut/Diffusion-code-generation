def repeat_and_merge(dictionary, repetitions):
    return {k: v * repetitions for k, v in dictionary.items()}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2}
    repetitions = 3
    result = repeat_and_merge(sample_dict, repetitions)
    print(result)