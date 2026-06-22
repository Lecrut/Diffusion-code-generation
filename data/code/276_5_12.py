def repeat_and_merge(dictionary, R):
    return {k: v * R for k, v in dictionary.items()}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2}
    repeated_merged_dict = repeat_and_merge(sample_dict, 3)
    print(repeated_merged_dict)