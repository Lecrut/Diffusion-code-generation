def check_lists_equal(list1, list2):
    return set(list1) == set(list2)

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9]
    sample_list2 = [9, 4, 3, 1, 5, 1]
    print(check_lists_equal(sample_list1, sample_list2))