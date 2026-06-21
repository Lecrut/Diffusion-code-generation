def merge_lists(list1, list2):
    result = list1.copy()
    result.extend(list2)
    return result

if __name__ == '__main__':
    sample_list_1 = [7, 8, 9]
    sample_list_2 = [10, 11, 12]
    merged_list = merge_lists(sample_list_1, sample_list_2)
    print(merged_list)