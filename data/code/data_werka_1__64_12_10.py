def find_final_item_index(indices):
    return max(indices) if indices else -1

if __name__ == '__main__':
    test_cases = [
        ([1, 5, 3, 8, 2], "Test Case 1"),
        ([10, 20, 5], "Test Case 2"),
        ([], "Test Case 3"),
        ([42], "Test Case 4"),
        ([-5, -1, -10], "Test Case 5")
    ]

    for indices, name in test_cases:
        print(f"Input: {indices}, Result: {find_final_item_index(indices)} ({name})")