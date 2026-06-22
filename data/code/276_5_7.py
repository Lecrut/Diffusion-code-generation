def repeat_and_merge(dictionary, R):
    result = {}
    for _ in range(R):
        result.update(dictionary)
    return result

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2}
    R = 3
    print(repeat_and_merge(sample_dict, R))