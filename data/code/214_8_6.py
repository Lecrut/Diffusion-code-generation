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
        ([-10, -5, -20, -1], -20),
        ([3.14, 1.618, 2.718], 1.618),
        ([-5, -1, -100, -50], -100),
        ([0, 0, 0, 0], 0),
        ([42], 42),
        ([], None)                                                                                       
    ]
    for input_list, expected in test_cases:
        try:
            result = find_minimum(input_list)
            assert result == expected, f"Input: {input_list}, Expected: {expected}, Got: {result}"
            print(f"Test Passed for {input_list}. Result: {result}")
        except ValueError as e:
            if expected is None:
                print(f"Test Passed for {input_list}. Caught expected error: {e}")
            else:
                print(f"Test Failed for {input_list}. Unexpected Error: {e}")
        except AssertionError as e:
            print(f"Test Failed for {input_list}. Assertion Error: {e}")
        except Exception as e:
            print(f"Test Failed for {input_list}. Unexpected Exception: {e}")