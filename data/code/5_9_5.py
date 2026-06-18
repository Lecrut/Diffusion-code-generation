import numpy as np

def compare_signs(length_a: np.ndarray, length_b: np.ndarray) -> np.ndarray:
    """
    Compare two arrays of length measurements element-wise.
    
    Returns an array where each value indicates the sign of (length_a[i] - length_b[i]):
        1 : positive difference
         0 : zero difference
        -1 : negative difference
    
    Assumes inputs are numpy arrays or lists convertible to them for performance.
    """
    # Convert input lists/tuples to NumPy array if necessary, then ensure float dtype
    arr_a = np.asarray(length_a, dtype=float)
    arr_b = np.asarray(length_b, dtype=float)

    # Calculate difference and apply sign using numpy's universal function 'sign' for speed
    return np.sign(arr_a - arr_b)

if __name__ == '__main__':
    # Hard-coded sample values running without user input or external dependencies
    
    array_1 = [3.5, 7.2, 4.0, 9.8]
    array_2 = [3.5, 6.0, 4.2, 9.8]

    result = compare_signs(array_1, array_2)

    print("Input Arrays:")
    print(f"Array A: {array_1}")
    print(f"Array B: {array_2}")
    
    print("\nSign of Differences (A - B):")
    print(result)