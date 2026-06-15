import numpy as np
def calculate_difference_of_extremes(arr: np.ndarray) -> float:
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a NumPy array.")
    if arr.size == 0:
        raise ValueError("Input array cannot be empty.")
    return np.max(arr) - np.min(arr)
if __name__ == '__main__':
    sample_array_1 = np.array([1, 5, 2, 8, 3])
    result_1 = calculate_difference_of_extremes(sample_array_1)
    print(f"Array: {sample_array_1}")
    print(f"Difference of extremes: {result_1}")
    sample_array_2 = np.array([-10, 0, 5, -5])
    result_2 = calculate_difference_of_extremes(sample_array_2)
    print(f"\nArray: {sample_array_2}")
    print(f"Difference of extremes: {result_2}")
    sample_array_3 = np.array([42])
    result_3 = calculate_difference_of_extremes(sample_array_3)
    print(f"\nArray: {sample_array_3}")
    print(f"Difference of extremes: {result_3}")
    try:
        sample_array_empty = np.array([])
        calculate_difference_of_extremes(sample_array_empty)
    except ValueError as e:
        print(f"\nHandling empty array error: {e}")