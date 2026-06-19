def find_last_occurrence_reverse(data, target):
    length = len(data)
    for index in range(length - 1, -1, -1):
        if data[index] == target:
            return index
    return -1

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_value_1 = 30
    result_index_1 = find_last_occurrence_reverse(sample_list_1, target_value_1)
    print(result_index_1)

    sample_list_2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    target_value_2 = 25
    result_index_2 = find_last_occurrence_reverse(sample_list_2, target_value_2)
    print(result_index_2)

    sample_list_3 = [1, 2, 3, 4, 5]
    target_value_3 = 6
    result_index_3 = find_last_occurrence_reverse(sample_list_3, target_value_3)
    print(result_index_3)