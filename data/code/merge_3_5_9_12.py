import numpy as np

def compare_signs(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    """
    Compare two NumPy arrays of length measurements element-wise.
    
    Returns an array where each element is the sign of (arr1[i] - arr2[i]).
    The result uses numpy's sign function for numerical robustness and performance,
    mapping positive differences to 1, negative to -1, and zero to 0.

    Parameters:
        arr1 (np.ndarray): First array of length measurements.
        arr2 (np.ndarray): Second array of length measurements.

    Returns:
        np.ndarray: Array containing the sign of the difference for each pair of elements.
    
    Performance Note:
        This implementation uses vectorized NumPy operations, avoiding Python loops
        to ensure high performance on large datasets.
    """
    diff = arr1 - arr2
    return np.sign(diff)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    length_measurements_1 = np.array([10.5, 23.7, 45.2, 67.8, 90.1])
    length_measurements_2 = np.array([10.0, 24.0, 45.0, 68.0, 90.0])

    result = compare_signs(length_measurements_1, length_measurements_2)

    print("Array 1:", length_measurements_1)
    print("Array 2:", length_measurements_2)
    print("Sign of difference (arr1 - arr2):", result)