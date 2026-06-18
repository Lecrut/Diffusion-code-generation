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
        np.ndarray: Array of signs (+1, -1, or 0) corresponding to the difference.
    """
    diff = a - b
    
    # Use numpy's sign function for performance and correctness with floats
    result = np.sign(diff.astype(float))
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, files, or network)
    measurements_a = np.array([10.5, 23.7, -4.2, 0.0, 99.9])
    measurements_b = np.array([10.0, 23.0, -4.0, 0.0, 100.0])

    result_array = compare_signs(measurements_a, measurements_b)

    print("Input Arrays:")
    print(f"A: {measurements_a}")
    print(f"B: {measurements_b}")
    
    print("\nSign of Difference (A - B):")
    print(result_array)