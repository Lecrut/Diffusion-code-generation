def repeat_and_merge_dict(d, v):
    result = {}
    for _ in range(v):
        for key, value in d.items():
            if isinstance(value, dict):
                result[key] = repeat_and_merge_dict(value, v)
            else:
                result[key] = value * v
    return result

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
    repeated_merged_dict = repeat_and_merge_dict(sample_dict, 3)
    print(repeated_merged_dict)