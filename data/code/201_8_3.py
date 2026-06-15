import numpy as np
def find_average(data):
    if not data:
        raise ValueError("Input data cannot be empty.")
    return sum(data) / len(data)
if __name__ == '__main__':
    test_set_1 = [1, 2, 3, 4, 5]
    expected_1 = 3.0
    result_1 = find_average(test_set_1)
    print(f"Test Set 1: {test_set_1}")
    print(f"Result: {result_1}, Expected: {expected_1}, Correct: {np.isclose(result_1, expected_1)}\n")
    test_set_2 = [10, 20, 30]
    expected_2 = 20.0
    result_2 = find_average(test_set_2)
    print(f"Test Set 2: {test_set_2}")
    print(f"Result: {result_2}, Expected: {expected_2}, Correct: {np.isclose(result_2, expected_2)}\n")
    test_set_3 = [1.5, 2.5, 3.5]
    expected_3 = 2.5
    result_3 = find_average(test_set_3)
    print(f"Test Set 3: {test_set_3}")
    print(f"Result: {result_3}, Expected: {expected_3}, Correct: {np.isclose(result_3, expected_3)}\n")
    test_set_4 = [7, 14, 21, 28]
    expected_4 = 19.5
    result_4 = find_average(test_set_4)
    print(f"Test Set 4: {test_set_4}")
    print(f"Result: {result_4}, Expected: {expected_4}, Correct: {np.isclose(result_4, expected_4)}\n")
    try:
        find_average([])
    except ValueError as e:
        print(f"Test Empty Set: Caught expected error: {e}\n")