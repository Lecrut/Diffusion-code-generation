def count_elements(sequence):
    return len(sequence)
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], 3),
        ("hello", 5),
        (range(0, 10), 10),
        ([], 0),
        ((True, False, True), 3)
    ]
    for i, (input_seq, expected_count) in enumerate(test_cases):
        result = count_elements(input_seq)
        assert result == expected_count, f"Test case {i} failed: Expected {expected_count}, got {result}"
    print("All test cases passed.")