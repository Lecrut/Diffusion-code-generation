def find_last_occurrence_reverse(data, target):
    for index in range(len(data) - 1, -1, -1):
        if data[index] == target:
            return index
    return -1

if __name__ == '__main__':
    sample_data_1 = [3, 5, 2, 7, 5, 9, 5, 8]
    target_value_1 = 5
    print(find_last_occurrence_reverse(sample_data_1, target_value_1))

    sample_data_2 = [10, 20, 30, 40, 50]
    target_value_2 = 60
    print(find_last_occurrence_reverse(sample_data_2, target_value_2))

    sample_data_3 = ['apple', 'banana', 'cherry', 'date', 'banana']
    target_value_3 = 'banana'
    print(find_last_occurrence_reverse(sample_data_3, target_value_3))