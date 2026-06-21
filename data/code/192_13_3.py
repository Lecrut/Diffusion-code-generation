def find_common_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    common_items = find_common_items(sample_list1, sample_list2)
    print(common_items)

    sample_list3 = ['apple', 'banana', 'cherry']
    sample_list4 = ['banana', 'date', 'apple']
    common_items = find_common_items(sample_list3, sample_list4)
    print(common_items)

    sample_list5 = [10, 20, 30]
    sample_list6 = [30, 10, 40]
    common_items = find_common_items(sample_list5, sample_list6)
    print(common_items)