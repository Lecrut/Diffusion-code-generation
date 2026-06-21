def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)

if __name__ == '__main__':
    sample_list_a = [1, 2, 2, 3, 4, 4]
    sample_list_b = [2, 4, 4, 5, 6]
    result1 = find_common_elements(sample_list_a, sample_list_b)
    print(result1)

    sample_list_c = ['apple', 'banana', 'cherry', 'apple', 'date']
    sample_list_d = ['date', 'fig', 'apple', 'grape']
    result2 = find_common_elements(sample_list_c, sample_list_d)
    print(result2)

    sample_list_e = [10, 20, 30]
    sample_list_f = [30, 10, 40]
    result3 = find_common_elements(sample_list_e, sample_list_f)
    print(result3)