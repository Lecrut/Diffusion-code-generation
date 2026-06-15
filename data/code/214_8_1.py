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
        ([], "Error: Input list cannot be empty"),
        ([100, 50, 25], 25)
    ]
    for input_list, expected_output in test_cases:
        try:
            actual_output = find_minimum(input_list)
            if actual_output == expected_output:
                print(f"Test Passed for {input_list}: Expected {expected_output}, Got {actual_output}")
            else:
                print(f"Test Failed for {input_list}: Expected {expected_output}, Got {actual_output}")
        except ValueError as e:
            if expected_output.startswith("Error"):
                print(f"Test Passed (Exception Handled) for {input_list}: {e}")
            else:
                print(f"Test Failed (Unexpected Exception) for {input_list}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {input_list}: {e}")