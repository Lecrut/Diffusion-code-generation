def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)

if __name__ == '__main__':
    sample_list_a = [5, 7, 8, 9, 9, 10]
    sample_list_b = [8, 9, 11, 12, 13, 9]
    result1 = find_common_elements(sample_list_a, sample_list_b)
    print(result1)

    sample_list_c = ['red', 'green', 'blue', 'red']
    sample_list_d = ['green', 'yellow', 'red', 'orange']
    result2 = find_common_elements(sample_list_c, sample_list_d)
    print(result2)

    sample_list_e = [15, 20, 25]
    sample_list_f = [30, 20, 15]
    result3 = find_common_elements(sample_list_e, sample_list_f)
    print(result3)