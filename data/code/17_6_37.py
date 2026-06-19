def is_even(number):
    return number % 2 == 0
test_cases = [(0, True), (-1, False), (-2, True), (1, False), (2, True), (3, False), (4, True), (5, False), (6, True)]
if __name__ == '__main__':
    for i, (input_value, expected_output) in enumerate(test_cases):
        result = is_even(input_value)
        print(f'Test case {i + 1}: is_even({input_value}) = {result} (expected: {expected_output})')