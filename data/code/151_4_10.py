def combine_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists.")
    return list(zip(list1, list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    combined_result = combine_lists(sample_list1, sample_list2)
    print(f"Combined list of {sample_list1} and {sample_list2}: {combined_result}")