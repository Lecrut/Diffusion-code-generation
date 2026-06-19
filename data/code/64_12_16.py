def find_final_item_index(indices):
    if not indices:
        return -1
    max_index = indices[0]
    for index in indices:
        if index > max_index:
            max_index = index
    return max_index

if __name__ == '__main__':
    sample_list_1 = [3, 7, 2, 9, 5]
    print(f"Input: {sample_list_1}, Result: {find_final_item_index(sample_list_1)}")
    
    sample_list_2 = []
    print(f"Input: {sample_list_2}, Result: {find_final_item_index(sample_list_2)}")
    
    sample_list_3 = [42]
    print(f"Input: {sample_list_3}, Result: {find_final_item_index(sample_list_3)}")
    
    sample_list_4 = [10, 10, 10]
    print(f"Input: {sample_list_4}, Result: {find_final_item_index(sample_list_4)}")
    
    sample_list_5 = [-2, -8, -1, -6]
    print(f"Input: {sample_list_5}, Result: {find_final_item_index(sample_list_5)}")