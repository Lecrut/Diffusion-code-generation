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
    list_c = ['apple', 'banana', 'cherry', 'apple', 'date']
    list_d = ['date', 'fig', 'apple', 'grape']
    result2 = find_common_elements(list_c, list_d)
    print(result2)
    list_e = [10, 20, 30]
    list_f = [30, 10, 40]
    result3 = find_common_elements(list_e, list_f)
    print(result3)