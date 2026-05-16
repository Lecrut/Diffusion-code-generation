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
    index_to_check = 2
    result = compare_elements(list_a, list_b, index_to_check)
    print(f"Comparing elements at index {index_to_check}: {result}")
    index_to_check = 0
    result = compare_elements(list_a, list_b, index_to_check)
    print(f"Comparing elements at index {index_to_check}: {result}")
    list_c = [1, 2, 3]
    list_d = [1, 2, 3]
    index_to_check = 1
    result = compare_elements(list_c, list_d, index_to_check)
    print(f"Comparing elements at index {index_to_check} (equal case): {result}")