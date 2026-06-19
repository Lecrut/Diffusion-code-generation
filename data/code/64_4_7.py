def find_last_index(data, value):
    last_index = -1
    for index in range(len(data) - 1, -1, -1):
        if data[index] == value:
            last_index = index
            break
    return last_index

if __name__ == '__main__':
    sample_list_1 = [3, 7, 9, 5, 7, 8]
    target_value_1 = 7
    result_1 = find_last_index(sample_list_1, target_value_1)
    print(f"List: {sample_list_1}, Value: {target_value_1}, Last Index: {result_1}")

    sample_list_2 = [10, 22, 33, 44, 55]
    target_value_2 = 66
    result_2 = find_last_index(sample_list_2, target_value_2)
    print(f"List: {sample_list_2}, Value: {target_value_2}, Last Index: {result_2}")

    sample_list_3 = [4, 4, 4, 4, 4]
    target_value_3 = 4
    result_3 = find_last_index(sample_list_3, target_value_3)
    print(f"List: {sample_list_3}, Value: {target_value_3}, Last Index: {result_3}")