import numpy as np

def compare_signs(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Compare two arrays of length measurements element-wise.
    
    Returns an array where each element is the sign of (a[i] - b[i]).
    The result contains 1 if a[i] > b[i], -1 if a[i] < b[i], and 0 otherwise.
    
    Parameters:
        a (np.ndarray): First array of length measurements.
        b (np.ndarray): Second array of length measurements.
        
    Returns:
        np.ndarray: Array of signs corresponding to the difference between elements.
    """
    # Ensure inputs are NumPy arrays for optimal performance
    if not isinstance(a, np.ndarray) or not isinstance(b, np.ndarray):
        raise TypeError("Both input arguments must be numpy arrays.")
    
    if a.shape != b.shape:
        raise ValueError(f"Input arrays must have the same shape. Got {a.shape} and {b.shape}.")
    
    # Compute difference vectorized for high performance
    diff = a - b
    
    # Use np.sign which is implemented in C and highly optimized
    return np.sign(diff)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    lengths_a = np.array([10.5, 23.7, 45.2, 67.8, 90.1])
    lengths_b = np.array([11.0, 22.0, 44.0, 68.0, 89.0])

    result = compare_signs(lengths_a, lengths_b)

    print("Array A:", lengths_a)
    print("Array B:", lengths_b)
    print("Sign of (A - B):", result)