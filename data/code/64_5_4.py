def find_final_match_reverse(data, target):
    n = len(data)
    if n == 0:
        return -1
    for i in range(n - 1, -1, -1):
        if data[i] == target:
            return i
    return -1
if __name__ == '__main__':
    large_list = [10, 20, 30, 40, 50, 50, 50, 60, 70, 80]
    target_value = 50
    result_index = find_final_match_reverse(large_list, target_value)
    print(result_index)
    large_list_2 = [1, 5, 3, 5, 9, 5, 2]
    target_value_2 = 5
    result_index_2 = find_final_match_reverse(large_list_2, target_value_2)
    print(result_index_2)
    large_list_3 = [100, 200, 300, 400]
    target_value_3 = 100
    result_index_3 = find_final_match_reverse(large_list_3, target_value_3)
    print(result_index_3)
    large_list_4 = [1, 2, 3, 4]
    target_value_4 = 99
    result_index_4 = find_final_match_reverse(large_list_4, target_value_4)
    print(result_index_4)