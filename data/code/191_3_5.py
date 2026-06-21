def combine_and_extend(list1, list2):
    if not all(isinstance(item, dict) for item in list1 + list2):
        raise ValueError("Both inputs must be lists of dictionaries")
    return list1 + list2

if __name__ == '__main__':
    sample_list1 = [{'a': 1}, {'b': 2}]
    sample_list2 = [{'c': 3}, {'d': 4}]
    combined_list = combine_and_extend(sample_list1, sample_list2)
    print(combined_list)