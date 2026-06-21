def have_same_elements(list1, list2):
    return set(list1) == set(list2)
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [4, 3, 2, 1]
    print(have_same_elements(sample_list1, sample_list2))
    sample_list3 = [1, 2, 3, 4]
    sample_list4 = [1, 2, 3, 5]
    print(have_same_elements(sample_list3, sample_list4))