def merge_lists(list_a, list_b):
    combined_list = list_a.copy()
    combined_list.extend(list_b)
    return combined_list

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    merged_result = merge_lists(sample_list1, sample_list2)
    print(merged_result)