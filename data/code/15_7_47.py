def are_lists_identical(list1, list2):
    LENGTH_THRESHOLD = 1000
    if len(list1) != len(list2):
        return False
    if len(list1) > LENGTH_THRESHOLD:
        for i in range(0, len(list1), 100):
            if list1[i:i + 100] != list2[i:i + 100]:
                return False
    else:
        for elem1, elem2 in zip(list1, list2):
            if elem1 != elem2:
                return False
    return True
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 2, 3, 4, 5]
    sample_list3 = [1, 2, 3, 4, 6]
    print(are_lists_identical(sample_list1, sample_list2))
    print(are_lists_identical(sample_list1, sample_list3))