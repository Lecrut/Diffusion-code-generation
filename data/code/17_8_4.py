def is_even(number):
    return number % 2 == 0
if __name__ == '__main__':
    test_cases = [
        (0, True),
        (1, False),
        (2, True),
        (-4, True),
        (-5, False),
        (100, True),
        (-1, False),
        (-2, True)
    ]
    for input_num, expected_output in test_cases:
        actual_output = is_even(input_num)
        assert actual_output == expected_output, f"Input: {input_num}, Expected: {expected_output}, Got: {actual_output}"
        print(f"Test passed for input {input_num}: is_even({input_num}) == {expected_output}")
    print("All test cases passed!")