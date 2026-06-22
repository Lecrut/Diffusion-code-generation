def compare_elements_at_index(list_a, list_b, index):
    if not isinstance(list_a, (list, tuple)):
        raise ValueError("First argument must be a list or tuple")
    if not isinstance(list_b, (list, tuple)):
        raise ValueError("Second argument must be a list or tuple")
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    if index < 0 or index >= len(list_a):
        raise ValueError("Index out of range for first list")
    if index < 0 or index >= len(list_b):
        raise ValueError("Index out of range for second list")

    val_a = list_a[index]
    val_b = list_b[index]

    if val_a > val_b:
        return 1
    elif val_a < val_b:
        return -1
    else:
        return 0

if __name__ == '__main__':
    first_list = [100, 200, 300]
    second_list = [100, 150, 300]
    target_index = 1
    comparison_result = compare_elements_at_index(first_list, second_list, target_index)
    print(comparison_result)
    
    third_list = [10, 20, 30]
    fourth_list = [10, 30, 30]
    another_index = 1
    another_result = compare_elements_at_index(third_list, fourth_list, another_index)
    print(another_result)
    
    fifth_list = [5, 10, 15]
    sixth_list = [5, 10, 15]
    equal_index = 2
    equal_result = compare_elements_at_index(fifth_list, sixth_list, equal_index)
    print(equal_result)