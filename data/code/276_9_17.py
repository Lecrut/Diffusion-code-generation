def repeat_and_merge_dict(nested_dict, v):
    result = {}
    for _ in range(v):
        for key, value in nested_dict.items():
            if isinstance(value, dict):
                if key not in result:
                    result[key] = {}
                repeat_and_merge_dict(value, v)
            else:
                if key not in result:
                    result[key] = []
                result[key].append(value)
    return result

if __name__ == '__main__':
    sample_dict = {
        'a': 1,
        'b': {'c': 2, 'd': {'e': 3}},
        'f': [4, 5]
    }
    repeated_merged_dict = repeat_and_merge_dict(sample_dict, 3)
    print(repeated_merged_dict)