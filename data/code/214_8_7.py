def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum
if __name__ == '__main__':
    test_cases = [
        ([5, 2, 8, 1], 1),
        ([-5, -10, -2, -1], -10),
        ([3.14, 1.618, 2.718], 1.618),
        ([-10, 0, 5, -15], -15),
        ([7], 7),
        ([], ValueError)
    ]
    for input_list, expected_result in test_cases:
        try:
            actual_result = find_minimum(input_list)
            if isinstance(expected_result, type):
                assert isinstance(actual_result, type), f"Expected error type, got {type(actual_result)}"
                print(f"Test Passed for input {input_list}: Raised expected error.")
            else:
                assert actual_result == expected_result, f"Input: {input_list}, Expected: {expected_result}, Got: {actual_result}"
                print(f"Test Passed for input {input_list}: Result {actual_result}")
        except ValueError as e:
            if isinstance(expected_result, type) and expected_result is ValueError:
                print(f"Test Passed for input {input_list}: Raised expected error: {e}")
            else:
                print(f"Test Failed for input {input_list}: Unexpected ValueError: {e}")
        except AssertionError as e:
            print(f"Test Failed for input {input_list}: Assertion Error: {e}")
        except Exception as e:
            print(f"Test Failed for input {input_list}: Unexpected Error: {e}")