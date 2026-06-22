def find_last_occurrence_reverse(data, target):
    for index in range(len(data) - 1, -1, -1):
        if data[index] == target:
            return index
    return -1

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_value = 30
    result_index = find_last_occurrence_reverse(sample_list, target_value)
    print(result_index)

    another_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    target_value_2 = 15
    result_index_2 = find_last_occurrence_reverse(another_list, target_value_2)
    print(result_index_2)

    no_match_list = [1, 2, 3, 4, 5]
    target_value_3 = 99
    result_index_3 = find_last_occurrence_reverse(no_match_list, target_value_3)
    print(result_index_3)