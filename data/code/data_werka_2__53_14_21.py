def compute_square_perimeter(side_length):
    if side_length < 0:
        raise ValueError('Side length cannot be negative')
    return 4 * side_length
if __name__ == '__main__':
    test_cases = [(0, 0), (1, 4), (2.5, 10), (10, 40)]
    for i, (side_length, expected) in enumerate(test_cases):
        result = compute_square_perimeter(side_length)
        assert result == expected, f'Test case {i + 1} failed: expected {expected}, got {result}'
    sample_side_length = 5
    perimeter = compute_square_perimeter(sample_side_length)
    print(perimeter)