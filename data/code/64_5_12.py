def find_last_match_reverse(data, target):
    index = -1
    for i in reversed(range(len(data))):
        if data[i] == target:
            index = i
            break
    return index

if __name__ == '__main__':
    large_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_value = 30
    result_index = find_last_match_reverse(large_list, target_value)
    print(result_index)

    large_list_2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    target_value_2 = 5
    result_index_2 = find_last_match_reverse(large_list_2, target_value_2)
    print(result_index_2)

    large_list_3 = [1, 2, 3, 4, 5]
    target_value_3 = 99
    result_index_3 = find_last_match_reverse(large_list_3, target_value_3)
    print(result_index_3)