def merge_lists(list_a, list_b):
    result_list = list_a.copy()
    result_list.extend(list_b)
    return result_list

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    merged_list = merge_lists(sample_list1, sample_list2)
    print(merged_list)