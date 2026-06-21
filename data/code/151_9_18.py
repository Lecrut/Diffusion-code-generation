def merge_lists(list_alpha, list_beta):
    result_set = set()
    for sublist in list_alpha:
        result_set.update(sublist)
    for sublist in list_beta:
        result_set.update(sublist)
    return result_set

if __name__ == '__main__':
    sample_list1 = [{1, 2}, {3, 4}]
    sample_list2 = [{5, 6}, {7, 8}]
    merged_result = merge_lists(sample_list1, sample_list2)
    print(merged_result)