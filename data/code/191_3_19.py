def combine_and_extend(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists")
    
    if not all(isinstance(item, dict) for item in list1 + list2):
        raise ValueError("All elements in both lists must be dictionaries")

    return list1 + list2

if __name__ == '__main__':
    sample_list1 = [{'a': 1}, {'b': 2}]
    sample_list2 = [{'c': 3}, {'d': 4}]
    combined_list = combine_and_extend(sample_list1, sample_list2)
    print(combined_list)