def find_common_elements(list1, list2):
    set2 = set(list2)
    return [item for item in list1 if item in set2]

if __name__ == '__main__':
    sample_list1 = [1, 2, 2, 3, 4, 4]
    sample_list2 = [2, 4, 4, 5, 6, 1]
    result = find_common_elements(sample_list1, sample_list2)
    print(result)