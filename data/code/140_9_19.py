def lists_contain_same_elements(list1: list, list2: list) -> bool:
    return len(list1) == len(list2) and set(list1).intersection(set(list2)) == set(list1)
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [4, 3, 2, 1]
    sample_list3 = [1, 2, 3, 5]
    print(lists_contain_same_elements(sample_list1, sample_list2))
    print(lists_contain_same_elements(sample_list1, sample_list3))