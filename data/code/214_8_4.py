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
        ([-5.5, -10.2, -3.1], -10.2),
        ([0, 0, 0, 0], 0),
        ([7], 7),
        ([], "Error: Input list cannot be empty"),
    ]
    for input_data, expected in test_cases:
        try:
            result = find_minimum(input_data)
            assert result == expected, f"Input: {input_data}, Expected: {expected}, Got: {result}"
            print(f"Test Passed for input {input_data}. Result: {result}")
        except ValueError as e:
            if expected.startswith("Error"):
                print(f"Test Passed (Expected Error) for input {input_data}. Error: {e}")
            else:
                print(f"Test Failed unexpectedly for input {input_data}. Error: {e}")
        except AssertionError as e:
            print(f"Test Failed for input {input_data}. Assertion Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for input {input_data}: {e}")