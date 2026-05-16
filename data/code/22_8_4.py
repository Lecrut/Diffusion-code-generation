def is_odd(number):
    return number % 2 != 0
if __name__ == '__main__':
    test_cases = [
        (4, False),
        (7, True),
        (0, False),
        (-3, True)
    ]
    for input_num, expected_output in test_cases:
        actual_output = is_odd(input_num)
        assert actual_output == expected_output, f"Input: {input_num}, Expected: {expected_output}, Got: {actual_output}"
        print(f"Test passed for input {input_num}")