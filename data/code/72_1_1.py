def compare_elements(list1, list2, index):
    val1 = list1[index]
    val2 = list2[index]
    if val1 > val2:
        return "list1 is greater"
    elif val1 < val2:
        return "list2 is greater"
    else:
        return "elements are equal"
if __name__ == '__main__':
    list_a = [10, 20, 30, 40]
    list_b = [15, 20, 35, 40]
    index_to_compare = 1
    result = compare_elements(list_a, list_b, index_to_compare)
    print(result)
    list_c = [5, 10, 15]
    list_d = [5, 12, 15]
    index_to_compare_2 = 1
    result_2 = compare_elements(list_c, list_d, index_to_compare_2)
    print(result_2)
    list_e = [1, 2, 3]
    list_f = [1, 2, 3]
    index_to_compare_3 = 0
    result_3 = compare_elements(list_e, list_f, index_to_compare_3)
    print(result_3)