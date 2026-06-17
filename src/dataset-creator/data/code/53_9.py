def count_elements(sequence):
    counter = 0
    for _ in sequence:
        counter += 1
    return counter
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], 3),
        (range(5), 5),
        ("hello", 5),
        ([], 0)
    ]
    for i, (seq, expected_count) in enumerate(test_cases):
        result = count_elements(seq)
        assert result == expected_count, f"Test case {i} failed: Expected {expected_count}, got {result}"
    print("All test cases passed.")