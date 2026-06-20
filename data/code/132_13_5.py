def lists_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] is not list2[i]:
            return False
    return True
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [1, 2, 3, 4]
    sample_list3 = [1, 2, 3, 5]
    print(lists_identical(sample_list1, sample_list2))
    print(lists_identical(sample_list1, sample_list3))