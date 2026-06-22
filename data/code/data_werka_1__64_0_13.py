def find_last_occurrence_index(data_list, item):
    last_index = -1
    for index in range(len(data_list) - 1, -1, -1):
        if data_list[index] == item:
            last_index = index
            break
    return last_index

if __name__ == '__main__':
    sample_list_1 = [3, 7, 2, 5, 8, 2, 9]
    target_item_1 = 2
    result_1 = find_last_occurrence_index(sample_list_1, target_item_1)
    print(f"List: {sample_list_1}, Item: {target_item_1}, Last Occurrence Index: {result_1}")

    sample_list_2 = ['x', 'y', 'z', 'x', 'w']
    target_item_2 = 'x'
    result_2 = find_last_occurrence_index(sample_list_2, target_item_2)
    print(f"List: {sample_list_2}, Item: {target_item_2}, Last Occurrence Index: {result_2}")

    sample_list_3 = [100, 200, 300]
    target_item_3 = 400
    result_3 = find_last_occurrence_index(sample_list_3, target_item_3)
    print(f"List: {sample_list_3}, Item: {target_item_3}, Last Occurrence Index: {result_3}")