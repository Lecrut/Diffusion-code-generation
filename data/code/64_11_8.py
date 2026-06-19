def find_final_item_index(item_indices):
    def is_valid_list(lst):
        return isinstance(lst, list) and all(isinstance(i, int) for i in lst)
    
    if not is_valid_list(item_indices):
        raise ValueError("Input must be a list of integers")
    
    if not item_indices:
        return -1
    
    return len(item_indices) - 1

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10],
        [],
        [7, 8, 9],
        [42]
    ]
    
    for idx, lst in enumerate(sample_lists):
        result = find_final_item_index(lst)
        print(f"Result for list {idx + 1}: {result}")