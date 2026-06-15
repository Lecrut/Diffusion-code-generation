import numpy as np
def find_average(data):
    if not data:
        raise ValueError("Input data cannot be empty.")
    return sum(data) / len(data)
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5], 3.0),
        ([10, 20, 30], 20.0),
        ([5.5, 6.5, 7.5], 6.5),
        ([-1, 1, 3, -3], 0.0),
        ([100], 100.0)
    ]
    for input_data, expected in test_cases:
        try:
            result = find_average(input_data)
            assert np.isclose(result, expected), f"Input: {input_data}, Expected: {expected}, Got: {result}"
            print(f"Test passed for input {input_data}: Result = {result}")
        except Exception as e:
            print(f"Test failed for input {input_data}. Error: {e}")
    try:
        find_average([], [0.0])
    except ValueError as e:
        print("Test passed for empty list: Caught expected error.")
    except Exception as e:
        print(f"Test failed for empty list: Caught unexpected error: {e}")