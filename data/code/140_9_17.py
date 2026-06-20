def lists_have_same_elements(list1, list2):
    return len(list1) == len(list2) and set(list1) == set(list2)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [4, 3, 2, 1]
    print(lists_have_same_elements(sample_list1, sample_list2))