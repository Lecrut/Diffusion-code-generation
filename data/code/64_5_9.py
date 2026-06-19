def is_valid_list(data):
    return isinstance(data, list)

def find_last_occurrence_reverse(data, target):
    if not is_valid_list(data):
        raise ValueError("The data must be a list.")
    
    n = len(data)
    for i in range(n - 1, -1, -1):
        if data[i] == target:
            return i
    return -1

if __name__ == '__main__':
    large_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_value = 30
    result_index = find_last_occurrence_reverse(large_list, target_value)
    print(result_index)

    large_list_2 = [5, 10, 15, 20, 25, 30, 35, 40]
    target_value_2 = 15
    result_index_2 = find_last_occurrence_reverse(large_list_2, target_value_2)
    print(result_index_2)

    large_list_3 = [1, 2, 3, 4, 5]
    target_value_3 = 99
    result_index_3 = find_last_occurrence_reverse(large_list_3, target_value_3)
    print(result_index_3)