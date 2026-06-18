def count_elements(sequence):
    return sum(1 for _ in sequence)
if __name__ == '__main__':
    test_cases = [
        ([10, 20, 30], 3),
        (range(5), 5),
        ("hello", 5),
        ([], 0),
    ]
    for index, (seq, expected) in enumerate(test_cases):
        result = count_elements(seq)
        assert result == expected, f"Test case {index + 1} failed: got {result}, expected {expected}"
    print("All test cases passed.")