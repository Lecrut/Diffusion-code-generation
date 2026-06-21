def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

def combine_and_merge(list1, list2):
    combined_list = list1 + list2
    merged_list = [merge_dictionaries(item1, item2) for item1, item2 in zip(combined_list[::2], combined_list[1::2])]
    return merged_list

if __name__ == '__main__':
    sample_list1 = [{'a': 1}, {'b': 2}]
    sample_list2 = [{'c': 3}, {'d': 4}]
    result = combine_and_merge(sample_list1, sample_list2)
    print(result)