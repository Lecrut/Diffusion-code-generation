def repeat_and_merge(dictionary, R):
    return {key: value for _ in range(R) for key, value in dictionary.items()}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2}
    R = 3
    result = repeat_and_merge(sample_dict, R)
    print(result)