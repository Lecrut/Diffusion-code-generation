def lists_are_equal(list1: list, list2: list) -> bool:
    return list1 == list2
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 2, 3, 4, 5]
    sample_list3 = [5, 4, 3, 2, 1]
    print(lists_are_equal(sample_list1, sample_list2))
    print(lists_are_equal(sample_list1, sample_list3))