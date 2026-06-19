def validate_input(data, target):
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")
    if not all(isinstance(item, (int, float, str)) for item in data):
        raise ValueError("All elements in the list must be int, float, or str.")
    if not isinstance(target, (int, float, str)):
        raise ValueError("Target must be int, float, or str.")

def find_last_occurrence_reverse(data, target):
    validate_input(data, target)
    n = len(data)
    for i in range(n - 1, -1, -1):
        if data[i] == target:
            return i
    return -1

if __name__ == '__main__':
    large_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_value = 70
    result_index = find_last_occurrence_reverse(large_list, target_value)
    print(result_index)

    large_list_2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    target_value_2 = 55
    result_index_2 = find_last_occurrence_reverse(large_list_2, target_value_2)
    print(result_index_2)

    large_list_3 = [1, 2, 3, 4, 5]
    target_value_3 = 99
    result_index_3 = find_last_occurrence_reverse(large_list_3, target_value_3)
    print(result_index_3)