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
        ([], None)                                                                                       
    ]
    for input_list, expected in test_cases:
        try:
            result = find_minimum(input_list)
            assert result == expected, f"Input: {input_list}, Expected: {expected}, Got: {result}"
            print(f"Test Passed for {input_list}: Result = {result}")
        except ValueError as e:
            if expected is None:
                print(f"Test Passed for {input_list}: Caught expected error: {e}")
            else:
                print(f"Test Failed for {input_list}: Unexpected ValueError: {e}")
        except AssertionError as e:
            print(f"Test Failed for {input_list}: Assertion Error: {e}")
        except Exception as e:
            print(f"Test Failed for {input_list}: Unexpected Error: {e}")