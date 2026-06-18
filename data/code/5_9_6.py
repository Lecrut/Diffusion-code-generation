import numpy as np

def compare_signs(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Compare two arrays of length measurements element-wise.
    
    Returns an array where each element is 1 if a[i] > b[i], 
    -1 if a[i] < b[i], and 0 otherwise.
    
    Parameters:
        a (np.ndarray): First array of float values.
        b (np.ndarray): Second array of float values.
        
    Returns:
        np.ndarray: Array of signs corresponding to the difference (a - b).
    """
    diff = a.astype(np.float64) - b.astype(np.float64)
    
    # Use sign function for robustness and performance with NumPy's C backend
    result = np.sign(diff)
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    length_measurements_a = np.array([10.5, 23.7, -4.2, 0.0, 99.9])
    length_measurements_b = np.array([10.0, 24.0, -4.0, 1.0, 98.0])

    result_array = compare_signs(length_measurements_a, length_measurements_b)

    print("Input Array A:", length_measurements_a)
    print("Input Array B:", length_measurements_b)
    print("Sign of Difference (A - B):", result_array)