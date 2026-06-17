def count_elements(sequence):
    counter = 0
    for _ in range(len(sequence)):
        counter += 1
    return counter
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], 3),
        (['a', 'b'], 2),
        ((True, False, True), 3),
        ([], 0)
    ]
    for input_seq, expected_count in test_cases:
        result = count_elements(input_seq)
        assert result == expected_count, f"Test failed for {input_seq}. Expected {expected_count}, got {result}"
    print("All tests passed.")