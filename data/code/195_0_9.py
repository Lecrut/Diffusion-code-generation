def lists_are_identical(list1, list2):
    return len(list1) == len(list2) and list1 == list2
if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [1, 2, 3]
    print(lists_are_identical(sample_list1, sample_list2))