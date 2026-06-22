def compare_list_elements(first_list, second_list, target_index):
    if not isinstance(first_list, (list, tuple)):
        raise ValueError("first_list must be a list or tuple")
    if not isinstance(second_list, (list, tuple)):
        raise ValueError("second_list must be a list or tuple")
    if not isinstance(target_index, int):
        raise ValueError("target_index must be an integer")
    if target_index < 0:
        target_index = len(first_list) + target_index
        target_index_2 = len(second_list) + target_index
    else:
        target_index_2 = target_index
    if target_index >= len(first_list) or target_index_2 >= len(second_list):
        raise IndexError("Index out of range for one or both lists")
    element_a = first_list[target_index]
    element_b = second_list[target_index_2]
    if element_a > element_b:
        return (1, element_a, element_b)
    if element_a < element_b:
        return (-1, element_a, element_b)
    return (0, element_a, element_b)

if __name__ == '__main__':
    data_x = [100, 200, 300]
    data_y = [100, 150, 300]
    pos = 1
    outcome = compare_list_elements(data_x, data_y, pos)
    print(outcome)
    data_p = [5, 6, 7]
    data_q = [5, 6, 8]
    pos_q = 2
    result_q = compare_list_elements(data_p, data_q, pos_q)
    print(result_q)