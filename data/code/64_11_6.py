def find_final_item_index(item_indices):
    if not item_indices:
        raise ValueError("Input list of indices cannot be empty")
    return len(item_indices) - 1

if __name__ == '__main__':
    sample_lists = [
        [1, 5, 2, 8, 3],
        [100],
        [],
        [42]
    ]
    
    for i, lst in enumerate(sample_lists):
        try:
            result = find_final_item_index(lst)
            print(f"Result for list {i+1}: {result}")
        except ValueError as e:
            print(f"Error for list {i+1}: {e}")