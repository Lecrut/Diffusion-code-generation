def lists_have_same_elements(lst1: list, lst2: list) -> bool:
    return len(lst1) == len(lst2) and set(lst1) == set(lst2)
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [4, 3, 2, 1]
    sample_list3 = [1, 2, 3, 5]
    print(lists_have_same_elements(sample_list1, sample_list2))
    print(lists_have_same_elements(sample_list1, sample_list3))