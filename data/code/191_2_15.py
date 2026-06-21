def merge_lists(list1, list2):
    return list(dict.fromkeys(list1 + list2))

if __name__ == '__main__':
    sample_list1 = [1.1, 2.2, 3.3, 4.4]
    sample_list2 = [3.3, 4.4, 5.5, 6.6]
    merged_list = merge_lists(sample_list1, sample_list2)
    print(merged_list)