def count_elements(sequence):
    counter = 0
    for _ in range(len(sequence)):
        counter += 1
    return counter
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], 3),
        (['a', 'b'], 2),
        ((10,), 1),
        ([], 0)
    ]
    for i, input_data in enumerate(test_cases):
        sequence = list(input_data[0]) if isinstance(input_data[0], tuple) else input_data[0]
        expected_count = input_data[1]
        result = count_elements(sequence)
        assert result == expected_count, f"Test case {i} failed. Expected {expected_count}, got {result}"
    print("All test cases passed.")