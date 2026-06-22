def compare_elements_at_index(list_a, list_b, index):
    if index < 0:
        raise ValueError("Index must be non-negative")
    if index >= len(list_a) or index >= len(list_b):
        raise IndexError("Index out of range for one or both lists")
    
    element_a = list_a[index]
    element_b = list_b[index]
    
    if element_a > element_b:
        return (1, element_a, element_b)
    elif element_a < element_b:
        return (-1, element_a, element_b)
    else:
        return (0, element_a, element_b)

if __name__ == '__main__':
    first_list = [10, 25, 40, 55]
    second_list = [10, 20, 40, 60]
    target_index = 1
    
    comparison_result = compare_elements_at_index(first_list, second_list, target_index)
    print(comparison_result)
    
    third_list = [5, 15, 25]
    fourth_list = [5, 15, 25]
    equal_index = 2
    
    equality_result = compare_elements_at_index(third_list, fourth_list, equal_index)
    print(equality_result)