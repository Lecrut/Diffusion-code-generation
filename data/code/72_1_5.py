def compare_elements(list1, list2, index):
    if index >= len(list1) or index >= len(list2):
        raise IndexError("Index out of bounds")
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
    index_to_check = 1
    result = compare_elements(list_a, list_b, index_to_check)
    print(f"Comparing elements at index {index_to_check}: {result}")
    list_c = [5, 10, 15]
    list_d = [5, 10, 20]
    index_to_check_2 = 2
    result_2 = compare_elements(list_c, list_d, index_to_check_2)
    print(f"Comparing elements at index {index_to_check_2}: {result_2}")
    list_e = [1, 2, 3]
    list_f = [1, 2, 3]
    index_to_check_3 = 0
    result_3 = compare_elements(list_e, list_f, index_to_check_3)
    print(f"Comparing elements at index {index_to_check_3}: {result_3}")