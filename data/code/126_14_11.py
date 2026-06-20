def lists_equal(list1: list, list2: list) -> bool:
    return list1 == list2
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [1, 2, 3, 4]
    sample_list3 = [4, 3, 2, 1]
    print(lists_equal(sample_list1, sample_list2))
    print(lists_equal(sample_list1, sample_list3))