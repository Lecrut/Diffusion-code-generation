def are_lists_identical(list1, list2):
    return set(list1) == set(list2)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [4, 3, 2, 1]
    print(are_lists_identical(sample_list1, sample_list2))