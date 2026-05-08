def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)
if __name__ == '__main__':
    list_a = [1, 2, 2, 3, 4, 4]
    list_b = [2, 4, 4, 5, 6]
    result1 = find_common_elements(list_a, list_b)
    print(result1)
    list_c = [10, 20, 30, 10]
    list_d = [30, 40, 30, 50]
    result2 = find_common_elements(list_c, list_d)
    print(result2)
    list_e = ['apple', 'banana', 'cherry', 'apple']
    list_f = ['banana', 'date', 'apple', 'fig']
    result3 = find_common_elements(list_e, list_f)
    print(result3)