def unique_common_items(list1, list2):
    return [item for item in set(list1) if item in set(list2)]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    print(unique_common_items(sample_list1, sample_list2))