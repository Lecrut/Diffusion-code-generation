def find_final_item_index(indices):
    if not indices:
        return -1
    return max(indices)

if __name__ == '__main__':
    test_cases = [
        ([1, 5, 3, 8, 2], "Test Case 1"),
        ([10, 20, 5], "Test Case 2"),
        ([], "Test Case 3"),
        ([42], "Test Case 4"),
        ([-5, -1, -10], "Test Case 5"),
    ]

    for indices, description in test_cases:
        result = find_final_item_index(indices)
        print(f"{description}: Input: {indices}, Result: {result}")