"""
Highly performant function to compare two arrays of length measurements 
and return an array indicating the sign of the difference between corresponding elements.

The sign function returns:
    1 if element > other (strict inequality)
   -1 if element < other
     0 otherwise (equal or NaN handling implicit via float behavior in NumPy ufuncs)

This implementation uses NumPy's vectorized operations for maximum performance on large arrays.
"""

import numpy as np

def compare_signs(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Compare two NumPy arrays element-wise and return the sign of their difference.

    Parameters
    ----------
    a : np.ndarray
        First array of length measurements (float or int).
    b : np.ndarray
        Second array of length measurements, same shape as `a`.

    Returns
    -------
    np.ndarray
        Array of signs: 
            1 if a[i] > b[i], -1 if a[i] < b[i], 0 otherwise.
    
    Performance Note
    ----------------
    This function uses NumPy's optimized ufuncs which are implemented in C, ensuring
    high performance even for very large arrays without explicit Python loops.

    Examples
    --------
    >>> import numpy as np
    >>> from compare_signs_function import compare_signs
    >>> arr1 = np.array([5, 3, 8])
    >>> arr2 = np.array([4, 6, 7])
    >>> compare_signs(arr1, arr2)
    array([ 1., -1.,  1.])
    
    """
    # Ensure inputs are NumPy arrays for vectorized operations and consistent behavior
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    if a.shape != b.shape:
        raise ValueError(f"Input arrays must have the same shape. Got {a.shape} and {b.shape}")

    # Use numpy.subtract for explicit difference calculation (slightly more readable than subtraction operator 
    # but effectively identical performance; ufuncs are highly optimized)
    diff = np.subtract(a, b)
    
    # Apply sign logic: 1 if positive, -1 if negative, 0 otherwise.
    # Using a custom lambda to avoid overhead of multiple conditional checks or ternary operations in compiled code.
    return np.sign(diff).astype(float)

if __name__ == '__main__':
    # Hard-coded sample values for testing and demonstration purposes.
    # No user input, network access, command-line arguments, or file I/O is required.

    # Sample data: length measurements in meters (floats)
    lengths_1 = np.array([50234.789, 60123.456, 45098.211])
    lengths_2 = np.array([49801.123, 60123.456, 45098.211])

    # Perform comparison and get the sign of differences
    result_signs = compare_signs(lengths_1, lengths_2)

    print("Array 1:", lengths_1)
    print("Array 2:", lengths_2)
    print("Signs (resulting array):", result_signs.astype(int))