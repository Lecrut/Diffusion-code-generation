import numpy as np

def compare_signs(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Compare two NumPy arrays element-wise and return an array of signs 
    representing a - b (positive if a > b, negative if a < b, zero otherwise).

    Parameters:
        a (np.ndarray): First input array.
        b (np.ndarray): Second input array.
    
    Returns:
        np.ndarray: An integer array where each element is 1, -1, or 0 
                    based on the sign of the difference between corresponding 
                    elements in a and b.

    Performance Note:
        This function uses vectorized NumPy operations to ensure high performance 
        for large arrays without explicit Python loops.
    """
    # Ensure inputs are numpy arrays
    a = np.asarray(a)
    b = np.asarray(b)
    
    if a.shape != b.shape:
        raise ValueError(f"Arrays must have the same shape, got {a.shape} and {b.shape}")

    diff = a - b
    
    sign_result = np.sign(diff.astype(float))
    
    # Convert floating point signs to integers (-1.0 -> -1, etc.)
    return sign_result.astype(int)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    arr_a = np.array([3.5, 7.2, -4.8, 0.0, 10])
    arr_b = np.array([3.0, 6.9, -5.0, 1.5, 10.1])

    result = compare_signs(arr_a, arr_b)
    
    # Print results for verification
    print("Array A:", arr_a.tolist())
    print("Array B:", arr_b.tolist())
    print("Sign of (A - B):", result.tolist())