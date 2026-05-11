def find_odd_numbers(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers
def test_find_odd_numbers():
    test_cases = [
        ([1, 2, 3, 4, 5], [1, 3, 5]),
        ([], []),
        ([2, 4, 6, 8], []),
        ([1, 3, 5, 7], [1, 3, 5, 7]),
        ([0, 2, 4, 6], []),
        ([101, 202, 303], [101, 303]),
        ([1], [1])
    ]
    for input_list, expected_output in test_cases:
        actual_output = find_odd_numbers(input_list)
        assert actual_output == expected_output, f"Input: {input_list}, Expected: {expected_output}, Got: {actual_output}"
        print(f"Test passed for input: {input_list}")
if __name__ == '__main__':
    test_find_odd_numbers()