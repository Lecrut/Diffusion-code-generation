def compare_elements_at_index(list_a, list_b, index):
    if not isinstance(list_a, (list, tuple)):
        raise ValueError("list_a must be a list or tuple")
    if not isinstance(list_b, (list, tuple)):
        raise ValueError("list_b must be a list or tuple")
    if not isinstance(index, int):
        raise ValueError("index must be an integer")
    if index < 0:
        index = len(list_a) + index
    if index < 0 or index >= len(list_a):
        raise IndexError("index out of range for list_a")
    if index < 0 or index >= len(list_b):
        raise IndexError("index out of range for list_b")
    
    element_a = list_a[index]
    element_b = list_b[index]
    
    if element_a > element_b:
        return (1, element_a, element_b)
    elif element_a < element_b:
        return (-1, element_a, element_b)
    else:
        return (0, element_a, element_b)

if __name__ == '__main__':
    data_one = [10, 25, 30, 45]
    data_two = [10, 20, 35, 45]
    target_index = 1
    comparison_result = compare_elements_at_index(data_one, data_two, target_index)
    print(comparison_result)
    
    data_three = [100, 200, 300]
    data_four = [100, 200, 300]
    equal_index = 2
    equality_result = compare_elements_at_index(data_three, data_four, equal_index)
    print(equality_result)
    
    data_five = [5, 10, 15]
    data_six = [5, 12, 15]
    less_index = 1
    less_result = compare_elements_at_index(data_five, data_six, less_index)
    print(less_result)