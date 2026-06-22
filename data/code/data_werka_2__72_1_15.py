def compare_elements_at_index(list_a, list_b, index):
    if index < 0 or index >= len(list_a) or index >= len(list_b):
        raise ValueError("Index out of bounds for one or both lists")
    element_a = list_a[index]
    element_b = list_b[index]
    if element_a > element_b:
        return (1, element_a, element_b)
    elif element_a < element_b:
        return (-1, element_a, element_b)
    return (0, element_a, element_b)

if __name__ == '__main__':
    sample_list_1 = [10, 25, 30, 40]
    sample_list_2 = [10, 20, 35, 40]
    target_index = 1
    comparison_result = compare_elements_at_index(sample_list_1, sample_list_2, target_index)
    print(comparison_result)
    sample_list_3 = [5, 10, 15]
    sample_list_4 = [5, 12, 15]
    target_index_2 = 1
    comparison_result_2 = compare_elements_at_index(sample_list_3, sample_list_4, target_index_2)
    print(comparison_result_2)
    sample_list_5 = [1, 2, 3]
    sample_list_6 = [1, 2, 3]
    target_index_3 = 2
    comparison_result_3 = compare_elements_at_index(sample_list_5, sample_list_6, target_index_3)
    print(comparison_result_3)