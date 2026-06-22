def repeat_and_merge_dict(input_dict, R):
    return {k: v * R for k, v in input_dict.items()}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2}
    repeated_times = 3
    result = repeat_and_merge_dict(sample_dict, repeated_times)
    print(result)