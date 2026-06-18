import numpy as np

def compare_signs(length_array_a: np.ndarray, length_array_b: np.ndarray) -> np.ndarray:
    """
    Compare two arrays of length measurements element-wise.
    
    Returns an array indicating the sign of the difference (a - b).
    Positive values correspond to 1, zero corresponds to 0, negative values correspond to -1.
    
    Args:
        length_array_a: Input numpy array of first set of lengths.
        length_array_b: Input numpy array of second set of lengths (must match shape of a).
        
    Returns:
        NumPy array containing signs as integers (-1, 0, or 1).
    """
    # Compute the difference vector using efficient NumPy broadcasting/operations
    diff = np.subtract(length_array_a, length_array_b)
    
    # Apply sign logic efficiently without loops: (diff >= 0) gives boolean array converted to int via casting
    signs = np.where(diff > 0, 1, -np.where(diff < 0, 1, 0))
    
    return signs

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    length_array_a = np.array([5.2, 3.8, 7.1, 4.9])
    length_array_b = np.array([6.0, 3.8, 7.0, 5.0])

    result = compare_signs(length_array_a, length_array_b)

    print("Array A:", length_array_a)
    print("Array B:", length_array_b)
    print("Sign of (A - B):", result)