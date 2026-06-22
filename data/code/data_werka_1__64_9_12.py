def find_final_index(data, target):
    last_index = -1
    for index, element in enumerate(data):
        if element == target:
            last_index = index
    return last_index

if __name__ == '__main__':
    sample_list_1 = [1, 5, 2, 8, 5, 3, 5, 9]
    target_value_1 = 5
    final_index_1 = find_final_index(sample_list_1, target_value_1)
    print(final_index_1)

    sample_list_2 = [10, 20, 30, 20, 40, 20]
    target_value_2 = 20
    final_index_2 = find_final_index(sample_list_2, target_value_2)
    print(final_index_2)

    sample_list_3 = [1, 2, 3, 4]
    target_value_3 = 99
    final_index_3 = find_final_index(sample_list_3, target_value_3)
    print(final_index_3)