import sys
def find_last_occurrence_index(data, item):
    last_index = -1
    for i in range(len(data)):
        if data[i] == item:
            last_index = i
    return last_index
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 5, 3, 5, 9]
    target_item = 5
    result = find_last_occurrence_index(sample_list, target_item)
    print(result)
    sample_list_2 = [10, 20, 30, 40]
    target_item_2 = 5
    result_2 = find_last_occurrence_index(sample_list_2, target_item_2)
    print(result_2)
    sample_list_3 = [1, 2, 3]
    target_item_3 = 4
    result_3 = find_last_occurrence_index(sample_list_3, target_item_3)
    print(result_3)
    sample_list_4 = []
    target_item_4 = 1
    result_4 = find_last_occurrence_index(sample_list_4, target_item_4)
    print(result_4)