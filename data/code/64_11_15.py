def is_valid_index_list(item_indices):
    return isinstance(item_indices, list) and all(isinstance(i, int) for i in item_indices)

def find_final_item_index(item_indices):
    if not is_valid_index_list(item_indices):
        raise ValueError("Input must be a list of integers")
    if not item_indices:
        return -1
    return len(item_indices) - 1

if __name__ == '__main__':
    sample_lists = [
        [1, 5, 2, 8, 3],
        [100],
        [],
        [42],
        [7, 8, 9, 10]
    ]
    
    for lst in sample_lists:
        result = find_final_item_index(lst)
        print(result)