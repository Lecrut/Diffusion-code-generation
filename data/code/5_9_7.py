import numpy as np

def sign_diff_array(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    """
    Computes an array of signs representing the difference between corresponding 
    elements in two input arrays.
    
    The result is -1 where arr1 < arr2, 0 where they are equal, and 1 where arr1 > arr2.
    
    Parameters:
        arr1 (np.ndarray): First array of length measurements.
        arr2 (np.ndarray): Second array of length measurements.
        
    Returns:
        np.ndarray: Array of signs (-1, 0, or 1) corresponding to the difference 
                    between elements in arr1 and arr2.
    
    Raises:
        ValueError: If input arrays do not have matching dimensions.
    """
    if len(arr1) != len(arr2):
        raise ValueError(f"Arrays must be of equal length, got {len(arr1)} and {len(arr2)}.")

    diff = arr1 - arr2
    
    # Use np.sign for high performance vectorized operation instead of conditional logic
    return np.sign(diff.astype(float))

if __name__ == '__main__':
    # Hard-coded sample values as requested, no user input or external dependencies.
    
    length_measurements_a = np.array([10.5, 23.7, 45.0, 67.8])
    length_measurements_b = np.array([10.0, 23.0, 45.0, 69.0])

    result = sign_diff_array(length_measurements_a, length_measurements_b)

    print("Input Array A:", length_measurements_a)
    print("Input Array B:", length_measurements_b)
    print("Sign of Difference (A - B):", result)
    
    # Verification breakdown:
    # 10.5 - 10.0 = 0.5 -> Positive (1)
    # 23.7 - 23.0 = 0.7 -> Positive (1)
    # 45.0 - 45.0 = 0.0   -> Zero (0)
    # 67.8 - 69.0 = -1.2 -> Negative (-1)