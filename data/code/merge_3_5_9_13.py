import numpy as np

def compare_signs(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Compare two arrays of length measurements element-wise.
    
    Returns an array where each element is +1 if a[i] > b[i], 
    -1 if a[i] < b[i], and 0 otherwise.
    
    Args:
        a (np.ndarray): First array of float values.
        b (np.ndarray): Second array of float values.
        
    Returns:
        np.ndarray: Array of signs (+1, -1, or 0) corresponding to the difference.
    """
    diff = a - b
    
    # Use sign function and map results to {-1, 0, 1} explicitly for clarity and performance
    result = np.sign(diff.astype(float))
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    measurements_a = np.array([1.5, 2.3, -0.7, 4.0, 0.0])
    measurements_b = np.array([1.6, 2.3, -0.8, 4.1, 0.1])

    result_array = compare_signs(measurements_a, measurements_b)

    print("Input Arrays:")
    print(f"A: {measurements_a}")
    print(f"B: {measurements_b}")
    
    print("\nSign of Differences (A - B):")
    for i in range(len(result_array)):
        diff_val = result_array[i]
        if diff_val == 1.0:
            sign_str = "+"
        elif diff_val == -1.0:
            sign_str = "-"
        else:
            sign_str = "0"
        
        print(f"{measurements_a[i]:>8} vs {measurements_b[i]:>8} -> {sign_str}")