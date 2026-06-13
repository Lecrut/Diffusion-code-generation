import numpy as np
def calculate_average(data):
    if not data:
        raise ValueError("Input data cannot be empty.")
    return sum(data) / len(data)
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5], 3.0),
        ([10, 20, 30], 20.0),
        ([5.5, 6.5, 7.5], 6.5),
        ([-1, 0, 1, 2, -1], 0.4),
        ([], None)                                    
    ]
    for input_data, expected in test_cases:
        try:
            result = calculate_average(input_data)
            assert np.isclose(result, expected), f"Input: {input_data}, Expected: {expected}, Got: {result}"
            print(f"Test Passed for input {input_data}: Result = {result}")
        except ValueError as e:
            if expected is None:
                print(f"Test Passed for input {input_data}: Caught expected error: {e}")
            else:
                print(f"Test Failed for input {input_data}: Unexpected error: {e}")
        except Exception as e:
            print(f"Test Failed unexpectedly for input {input_data}: {e}")