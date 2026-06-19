def find_final_item_index(indices):
    EMPTY_LIST_RESULT = -1
    if not indices:
        return EMPTY_LIST_RESULT
    return max(indices)

if __name__ == '__main__':
    sample_lists = [
        [1, 5, 3, 8, 2],
        [],
        [42],
        [-5, -1, -10],
        [10, 20, 5],
        [100],
        [5, 5, 5],
        [-10, 0, -5]
    ]
    
    for i, lst in enumerate(sample_lists):
        print(f"Sample {i+1}: Input: {lst}, Result: {find_final_item_index(lst)}")