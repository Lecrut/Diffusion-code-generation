def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)

if __name__ == '__main__':
    sample_list1 = [5, 7, 9, 9, 10]
    sample_list2 = [8, 9, 9, 10, 11]
    common_result = find_common_elements(sample_list1, sample_list2)
    print(common_result)

    sample_list3 = ['red', 'green', 'blue', 'red']
    sample_list4 = ['green', 'yellow', 'blue', 'green']
    common_result = find_common_elements(sample_list3, sample_list4)
    print(common_result)

    sample_list5 = [100, 200, 300]
    sample_list6 = [300, 400, 500]
    common_result = find_common_elements(sample_list5, sample_list6)
    print(common_result)