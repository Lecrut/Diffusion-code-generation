import numpy as np

def compare_signs(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Compare two arrays of length measurements element-wise.
    
    Returns an array where each element is +1 if a[i] > b[i], 
    -1 if a[i] < b[i], and 0 otherwise.
    
    Parameters:
        a (np.ndarray): First array of float values.
        b (np.ndarray): Second array of float values.
        
    Returns:
        np.ndarray: Array of signs (+1, -1, or 0) corresponding to the difference (a[i] - b[i]).
    
    Performance Note:
        Uses NumPy's vectorized operations for maximum performance on large datasets.
    """
    # Ensure inputs are numpy arrays and compute differences directly in a single operation
    diff = np.asarray(a, dtype=float) - np.asarray(b, dtype=float)
    
    # Use sign function which is highly optimized in NumPy (C-level implementation)
    return np.sign(diff)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample array 1: Length measurements in meters
    lengths_a = np.array([10.5, 23.7, -4.2, 0.0, 99.9])
    
    # Sample array 2: Reference length measurements in meters
    lengths_b = np.array([10.0, 24.0, -4.0, 0.5, 98.0])
    
    result = compare_signs(lengths_a, lengths_b)
    
    print("Input Arrays:")
    print(f"A: {lengths_a}")
    print(f"B: {lengths_b}")
    print("\nSign of Difference (A - B):")
    print(result)