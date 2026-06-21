def get_unique_common_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_items = set1 & set2
    return common_items

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    print(get_unique_common_items(sample_list1, sample_list2))