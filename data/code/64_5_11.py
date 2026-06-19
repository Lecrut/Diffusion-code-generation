def find_last_index_reverse(data, target):
    index = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] == target:
            index = i
            break
    return index

if __name__ == '__main__':
    sample_list_1 = [5, 10, 15, 20, 15, 25, 30, 15]
    target_value_1 = 15
    result_index_1 = find_last_index_reverse(sample_list_1, target_value_1)
    print(result_index_1)

    sample_list_2 = [100, 200, 300, 400, 500]
    target_value_2 = 600
    result_index_2 = find_last_index_reverse(sample_list_2, target_value_2)
    print(result_index_2)

    sample_list_3 = [1, 1, 1, 1, 1]
    target_value_3 = 1
    result_index_3 = find_last_index_reverse(sample_list_3, target_value_3)
    print(result_index_3)