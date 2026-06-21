def lists_are_identical(list1, list2):
    return len(list1) == len(list2) and all((x == y for x, y in zip(list1, list2)))
if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [1, 2, 3]
    print(lists_are_identical(sample_list1, sample_list2))
    sample_list3 = [1, 2, 3]
    sample_list4 = [1, 2, 4]
    print(lists_are_identical(sample_list3, sample_list4))