import numpy as np

def compare_signs(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Compare two arrays of length measurements element-wise.
    
    Returns an array where each element is +1 if a[i] > b[i], 
    -1 if a[i] < b[i], and 0 if they are equal.
    
    Parameters:
        a (np.ndarray): First array of float values.
        b (np.ndarray): Second array of float values.
        
    Returns:
        np.ndarray: Array of signs (+1, -1, or 0) corresponding to the difference (a[i] - b[i]).
    
    Performance Note:
        This implementation uses NumPy's vectorized operations exclusively 
        to ensure high performance on large datasets without Python loops.
    """
    # Ensure inputs are numpy arrays for consistent behavior and speedup
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    
    # Compute the difference directly using vectorized subtraction
    diff = a - b
    
    # Use sign function which is highly optimized in NumPy C backend.
    # It returns 1 for positive, -1 for negative, and 0 for zero.
    return np.sign(diff)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Sample array A: Length measurements in meters (simulated data)
    arr_a = np.array([10.5, 23.4, -5.0, 0.0, 7.8])
    
    # Sample array B: Reference length measurements in meters
    arr_b = np.array([9.5, 23.4, -6.0, 0.1, 7.8])
    
    result = compare_signs(arr_a, arr_b)
    
    print("Array A:", arr_a)
    print("Array B:", arr_b)
    print("Sign of difference (A - B):", result)