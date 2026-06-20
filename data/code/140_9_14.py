def lists_have_same_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return len(set1) == len(set2) and set1.intersection(set2) == set1
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [4, 3, 2, 1]
    sample_list3 = [1, 2, 3, 5]
    print(lists_have_same_elements(sample_list1, sample_list2))
    print(lists_have_same_elements(sample_list1, sample_list3))