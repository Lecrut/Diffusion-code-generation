def find_final_index(data_list, target_item):
    last_index = -1
    for index, item in enumerate(data_list):
        if item == target_item:
            last_index = index
    return last_index

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 2, 5, 2]
    target = 2
    print(find_final_index(sample_data, target))