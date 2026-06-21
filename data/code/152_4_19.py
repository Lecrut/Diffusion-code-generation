def find_common_elements(list1, list2):
    set2 = set(list2)
    common = [element for element in list1 if element in set2]
    return common

if __name__ == '__main__':
    sample_list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    sample_list2 = [0, 1, 2, 3, 4, 5]
    result = find_common_elements(sample_list1, sample_list2)
    print(result)