def are_lists_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    return all(elem1 == elem2 for elem1, elem2 in zip(list1, list2))

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [10, 20, 30, 40, 50]
    sample_list3 = [10, 20, 30, 40, 60]
    print(are_lists_identical(sample_list1, sample_list2))
    print(are_lists_identical(sample_list1, sample_list3))