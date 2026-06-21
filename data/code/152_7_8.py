def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)

if __name__ == '__main__':
    list_a = [5, 6, 7, 8, 9, 9]
    list_b = [7, 8, 8, 10, 11]
    result1 = find_common_elements(list_a, list_b)
    print(result1)
    
    list_c = ['apple', 'banana', 'cherry', 'date']
    list_d = ['banana', 'grape', 'kiwi', 'apple']
    result2 = find_common_elements(list_c, list_d)
    print(result2)
    
    list_e = [100, 200, 300, 400]
    list_f = [300, 500, 600, 700]
    result3 = find_common_elements(list_e, list_f)
    print(result3)