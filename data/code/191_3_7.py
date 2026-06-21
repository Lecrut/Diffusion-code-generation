def validate_lists(list1, list2):
    if not all(isinstance(item, dict) for item in list1 + list2):
        raise ValueError("Both lists must contain only dictionaries.")

def combine_dicts(dict1, dict2):
    return {**dict1, **dict2}

def combine_and_merge_lists(list1, list2):
    validate_lists(list1, list2)
    combined_list = [combine_dicts(d1, d2) for d1, d2 in zip(list1, list2)]
    return combined_list

if __name__ == '__main__':
    sample_list1 = [{'a': 1}, {'b': 2}]
    sample_list2 = [{'c': 3}, {'d': 4}]
    result = combine_and_merge_lists(sample_list1, sample_list2)
    print(result)