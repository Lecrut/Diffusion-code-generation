def merge_lists(list_a, list_b):
    return [*list_a, *list_b]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    merged_result = merge_lists(sample_list1, sample_list2)
    print(merged_result)