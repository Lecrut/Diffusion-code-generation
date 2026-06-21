def find_unique_common_items(list1, list2):
    common_set = set()
    for item in list1:
        if item in list2 and item not in common_set:
            common_set.add(item)
    return list(common_set)

if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7, 9]
    sample_list2 = [0, 2, 4, 6, 8, 7, 5]
    print(find_unique_common_items(sample_list1, sample_list2))