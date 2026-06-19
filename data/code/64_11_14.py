def find_final_item_index(item_indices):
    return len(item_indices) - 1 if item_indices else -1

if __name__ == '__main__':
    test_cases = [
        [1, 5, 2, 8, 3],
        [100],
        [],
        [42]
    ]
    for i, case in enumerate(test_cases):
        result = find_final_item_index(case)
        print(f"Test Case {i+1}: List {case} -> Final Item Index: {result}")