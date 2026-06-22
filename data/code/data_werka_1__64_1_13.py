def find_final_index(data_list, target_item):
    index = -1
    for i in range(len(data_list)):
        if data_list[i] == target_item:
            index = i
    return index

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 2, 5, 2]
    target = 2
    print(find_final_index(sample_data, target))