def compute_square_perimeter(side_length):
    if side_length < 0:
        raise ValueError('Side length cannot be negative')
    return 4 * side_length

if __name__ == '__main__':
    test_cases = [
        (0, 0),
        (1, 4),
        (2.5, 10),
        (10, 40)
    ]
    for i, (input_value, expected_output) in enumerate(test_cases):
        try:
            result = compute_square_perimeter(input_value)
            assert result == expected_output, f'Test case {i + 1} failed: input({input_value}) => output({result}), expected({expected_output})'
        except AssertionError as e:
            print(e)

    sample_side_length = 3
    try:
        perimeter = compute_square_perimeter(sample_side_length)
        print(perimeter)
    except ValueError as e:
        print(e)