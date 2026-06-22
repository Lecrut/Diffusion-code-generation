def find_final_item_index(indices):
    if not indices:
        return -1
    return max(indices)

if __name__ == '__main__':
    SAMPLE_LISTS = [
        [1, 5, 3, 8, 2],
        [],
        [100],
        [42],
        [-5, -1, -10]
    ]
    
    for i, lst in enumerate(SAMPLE_LISTS):
        print(f"Input: {lst}, Result: {find_final_item_index(lst)}")