import numpy as np

def compare_signs(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    """
    Compare two NumPy arrays element-wise and return an array of signs 
    representing the difference between corresponding elements.
    
    The sign is determined by (arr1 - arr2):
        1 if arr1 > arr2
         0 if arr1 == arr2
        -1 if arr1 < arr2
    
    Parameters:
        arr1 (np.ndarray): First array of length measurements.
        arr2 (np.ndarray): Second array of length measurements.
    
    Returns:
        np.ndarray: Array containing the sign differences (-1, 0, or 1).
    """
    # Ensure inputs are NumPy arrays for optimal performance and type consistency
    if not isinstance(arr1, np.ndarray) or not isinstance(arr2, np.ndarray):
        raise TypeError("Both input arguments must be numpy arrays.")

    diff = arr1 - arr2
    
    return np.sign(diff).astype(int)

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input
    lengths_1 = np.array([10.5, 20.3, 30.7, 40.1])
    lengths_2 = np.array([9.8, 20.3, 31.2, 39.6])

    result = compare_signs(lengths_1, lengths_2)
    
    print("Input Arrays:")
    print(f"Array 1: {lengths_1}")
    print(f"Array 2: {lengths_2}")
    print("\nSign Differences (-1 if arr1 < arr2, 0 if equal, 1 if arr1 > arr2):")
    print(result)

    # Verification of expected output logic manually for clarity in comments
    # Expected result based on manual calculation: [1, 0, -1, 1]