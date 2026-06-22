def are_identical_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 2, 3, 4, 5]
    sample_list3 = [1, 2, 3, 4, 6]
    print(are_identical_lists(sample_list1, sample_list2))
    print(are_identical_lists(sample_list1, sample_list3))