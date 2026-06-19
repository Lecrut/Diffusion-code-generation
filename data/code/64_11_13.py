def find_final_item_index(item_indices):
    if not item_indices:
        return -1
    last_index = len(item_indices) - 1
    return last_index
if __name__ == '__main__':
    sample_list_1 = [7, 3, 9, 2, 5]
    print(find_final_item_index(sample_list_1))
    sample_list_2 = [100]
    print(find_final_item_index(sample_list_2))
    sample_list_3 = []
    print(find_final_item_index(sample_list_3))
    sample_list_4 = [42, 84, 168]
    print(find_final_item_index(sample_list_4))