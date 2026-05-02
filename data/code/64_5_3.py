def find_final_match_reverse(data, target):
    n = len(data)
    if n == 0:
        return -1
    for i in range(n - 1, -1, -1):
        if data[i] == target:
            return i
    return -1
if __name__ == '__main__':
    large_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_value = 70
    result_index = find_final_match_reverse(large_list, target_value)
    print(result_index)
    large_list_2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    target_value_2 = 55
    result_index_2 = find_final_match_reverse(large_list_2, target_value_2)
    print(result_index_2)
    large_list_3 = [1, 2, 3, 4, 5]
    target_value_3 = 1
    result_index_3 = find_final_match_reverse(large_list_3, target_value_3)
    print(result_index_3)
    large_list_4 = [100, 50, 30, 20, 10]
    target_value_4 = 100
    result_index_4 = find_final_match_reverse(large_list_4, target_value_4)
    print(result_index_4)
    large_list_5 = [1, 1, 1, 1, 1]
    target_value_5 = 1
    result_index_5 = find_final_match_reverse(large_list_5, target_value_5)
    print(result_index_5)
    large_list_6 = [1, 2, 3, 4, 5]
    target_value_6 = 99
    result_index_6 = find_final_match_reverse(large_list_6, target_value_6)
    print(result_index_6)