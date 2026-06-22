def repeat_and_merge_dict(d, V):
    return {k: v * V for k, v in d.items()}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2}
    repeated_merged_dict = repeat_and_merge_dict(sample_dict, 3)
    print(repeated_merged_dict)