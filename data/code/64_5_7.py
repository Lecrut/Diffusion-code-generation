def find_last_occurrence_reverse(data, target):
    if not isinstance(data, list):
        raise ValueError("The data must be a list.")
    if not isinstance(target, (int, float, str)):
        raise ValueError("The target must be an int, float, or string.")
    
    n = len(data)
    for i in range(n - 1, -1, -1):
        if data[i] == target:
            return i
    return -1

if __name__ == '__main__':
    large_list_1 = [10, 20, 30, 40, 20, 50, 30, 60, 20]
    target_value_1 = 20
    try:
        result_index_1 = find_last_occurrence_reverse(large_list_1, target_value_1)
        print(result_index_1)
    except ValueError as e:
        print(e)

    large_list_2 = ['apple', 'banana', 'cherry', 'date', 'banana']
    target_value_2 = 'banana'
    try:
        result_index_2 = find_last_occurrence_reverse(large_list_2, target_value_2)
        print(result_index_2)
    except ValueError as e:
        print(e)

    large_list_3 = [1.5, 2.5, 3.5, 4.5]
    target_value_3 = 99.9
    try:
        result_index_3 = find_last_occurrence_reverse(large_list_3, target_value_3)
        print(result_index_3)
    except ValueError as e:
        print(e)

    large_list_4 = [True, False, True]
    target_value_4 = False
    try:
        result_index_4 = find_last_occurrence_reverse(large_list_4, target_value_4)
        print(result_index_4)
    except ValueError as e:
        print(e)