import numpy as np

def compare_signs(length_array_a: np.ndarray, length_array_b: np.ndarray) -> np.ndarray:
    """
    Compare two arrays of length measurements element-wise and return an array indicating 
    the sign of the difference (a - b).
    
    Returns 1 if a > b, -1 if a < b, and 0 if equal.
    Uses vectorized NumPy operations for high performance without explicit Python loops.

    Parameters:
        length_array_a (np.ndarray): First array of lengths or measurements.
        length_array_b (np.ndarray): Second array of lengths or measurements. Must be same shape as a.

    Returns:
        np.ndarray: Array containing 1, -1, or 0 based on the comparison result.
    
    Raises:
        ValueError: If input arrays have different shapes.
        TypeError: If inputs are not numpy arrays or lists convertible to them.
    """
    # Ensure both inputs are NumPy arrays for efficient computation
    arr_a = np.asarray(length_array_a)
    arr_b = np.asarray(length_array_b)

    if arr_a.shape != arr_b.shape:
        raise ValueError(f"Input arrays must have the same shape. Got {arr_a.shape} and {arr_b.shape}")

    # Compute element-wise difference vectorizedly
    diff = arr_a - arr_b
    
    # Use np.sign to get {-1, 0, 1}, then adjust mapping if needed (optional)
    # Standard sign function returns exactly what is required: 1 for positive, -1 for negative, 0 otherwise.

    return np.sign(diff.astype(float))

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or external files needed)
    
    a = [3.5, 7.2, 4.8, 10.0]
    b = [6.5, 7.2, 9.0, 10.0]

    # Convert lists to NumPy arrays for processing
    arr_a = np.array(a)
    arr_b = np.array(b)

    result_arr = compare_signs(arr_a, arr_b)

    print("Input Arrays:")
    print(f"Array A: {arr_a}")
    print(f"Array B: {arr_b}")

    print("\nComparison Result (Sign of A - B):")
    for i in range(len(result_arr)):
        diff_val = result_arr[i]
        if abs(diff_val) > 1e-9: # Float comparison tolerance check logic implicitly handled by sign, but explicit clarity here
            direction = "greater" if diff_val == 1 else "less"
            print(f"Index {i}: A[{i}] is {direction} than B[{i}]")
        else:
            print(f"Index {i}: A[{i}] equals B[{i}] (diff sign)")

    # Verify the output matches expectations
    expected_signs = np.array([1, -1.0, 1, 0]) 
    assert np.allclose(result_arr.astype(int), expected_signs), "Comparison result does not match expected values."