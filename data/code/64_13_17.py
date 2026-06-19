def find_final_index(indices):
    if not indices:
        return -1
    last_index = indices[-1]
    return last_index

if __name__ == '__main__':
    test_cases = [
        [7, 3, 5, 9, 2],
        [4, 8, 15, 16, 23, 42],
        [100],
        [],
        [42, 99, 12, 55]
    ]
    
    for i, indices in enumerate(test_cases):
        result = find_final_index(indices)
        print(f"Test case {i+1}: {result}")