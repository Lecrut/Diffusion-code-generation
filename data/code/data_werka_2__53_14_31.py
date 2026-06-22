def compute_square_perimeter(side_length):
    if side_length < 0:
        raise ValueError('Side length cannot be negative')
    return 4 * side_length

if __name__ == '__main__':
    TEST_CASES = [
        (0, 0),
        (1, 4),
        (2.5, 10),
        (10, 40)
    ]
    
    for i, (input_value, expected_output) in enumerate(TEST_CASES):
        result = compute_square_perimeter(input_value)
        assert result == expected_output, f'Test case {i + 1} failed: input({input_value}) => output({result}), expected({expected_output})'
    
    SAMPLE_SIDE_LENGTH = 7
    perimeter = compute_square_perimeter(SAMPLE_SIDE_LENGTH)
    print(perimeter)