def find_last_index(data_list, target):
    for index in range(len(data_list) - 1, -1, -1):
        if data_list[index] == target:
            return index
    return -1

if __name__ == '__main__':
    sample_data = [5, 3, 9, 1, 3, 7, 3]
    target_value = 3
    last_index = find_last_index(sample_data, target_value)
    print(f"The last occurrence of {target_value} is at index: {last_index}")
    
    sample_data_empty = []
    target_empty = 5
    last_index_empty = find_last_index(sample_data_empty, target_empty)
    print(f"The last occurrence of {target_empty} in an empty list is at index: {last_index_empty}")
    
    sample_data_single = [10]
    target_single = 10
    last_index_single = find_last_index(sample_data_single, target_single)
    print(f"The last occurrence of {target_single} in a single-element list is at index: {last_index_single}")