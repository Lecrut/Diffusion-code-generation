def are_lists_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    for a, b in zip(list1, list2):
        if a != b:
            return False
    return True

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 2, 3, 4, 5]
    print(are_lists_identical(sample_list1, sample_list2))