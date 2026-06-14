def find_minimum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    test_cases = [
        ([1, 5, 2, 8], 1),
        ([-10, -5, -20, -1], -20),
        ([3.14, 1.618, 2.718], 1.618),
        ([-5, 0, 5, -10], -10),
        ([7], 7),
        ([], "Error"),
        ([5, 5, 5], 5)
    ]
    for input_list, expected_output in test_cases:
        try:
            result = find_minimum(input_list)
            if result == expected_output:
                print(f"Test Passed for {input_list}: Result={result}, Expected={expected_output}")
            else:
                print(f"Test Failed for {input_list}: Result={result}, Expected={expected_output}")
        except ValueError as e:
            if expected_output == "Error":
                 print(f"Test Passed (Exception Handled) for {input_list}: Caught expected error: {e}")
            else:
                print(f"Test Failed for {input_list}: Unexpected Error: {e}")
        except Exception as e:
            print(f"Test Failed for {input_list}: An unexpected error occurred: {e}")