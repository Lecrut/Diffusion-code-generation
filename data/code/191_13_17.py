def merge_lists(list1, list2):
    list1.extend(list2)
    return list1

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    merged_list = merge_lists(sample_list1, sample_list2)
    print(merged_list)