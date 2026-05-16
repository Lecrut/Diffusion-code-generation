def find_final_index(indices):
    if not indices:
        return -1
    return max(indices)
if __name__ == '__main__':
    test_cases = [
        ([], -1),
        ([5], 5),
        ([1, 8, 3], 8),
        ([10, 2, 5], 10),
        ([-1, -5, -2], -1),
        ([0, 0, 0], 0),
        ([100, 50, 25], 100)
    ]
    for input_list, expected in test_cases:
        result = find_final_index(input_list)
        assert result == expected, f"Input: {input_list}, Expected: {expected}, Got: {result}"
        print(f"Input: {input_list}, Result: {result} (Passed)")