def append_lists(list1, list2):
    list1 += list2

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    append_lists(sample_list1, sample_list2)
    print("Updated List 1:", sample_list1)