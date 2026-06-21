def compare_list_elements(list_first, list_second, index):
    if index < 0 or index >= len(list_first) or index >= len(list_second):
        raise ValueError("Index out of range for one or both lists")
    element_first = list_first[index]
    element_second = list_second[index]
    if element_first > element_second:
        return (1, element_first, element_second)
    if element_first < element_second:
        return (-1, element_first, element_second)
    return (0, element_first, element_second)

if __name__ == '__main__':
    sample_list_one = [10, 20, 30, 40]
    sample_list_two = [15, 20, 25, 40]
    target_index = 1
    comparison_result = compare_list_elements(sample_list_one, sample_list_two, target_index)
    print(comparison_result)
    sample_list_three = [5, 10, 15]
    sample_list_four = [5, 12, 15]
    target_index_two = 1
    comparison_result_two = compare_list_elements(sample_list_three, sample_list_four, target_index_two)
    print(comparison_result_two)