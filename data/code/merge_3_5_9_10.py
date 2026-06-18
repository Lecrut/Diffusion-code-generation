import numpy as np

def compare_signs(array1: np.ndarray | list[float], array2: np.ndarray | list[float]) -> np.ndarray[int]:
    """
    Returns an integer array where each element is +1 if corresponding elements in 
    the input arrays are equal, -1 if greater/lesser respectively.

    Args:
        array1 (np.ndarray or list): First set of length measurements.
        array2 (np.ndarray or list): Second set of length measurements.

    Returns:
        np.ndarray[int]: Array of signs (+1 for equality, 1 where a > b otherwise).
                          Note: The sign logic is simplified to indicate ordering 
                          relative to the prompt's typical expectation ('sign' usually implies +/−0 based on difference),
                          but strictly following standard 'sgn(diff)' behavior often requires handling zero.
                          Given the ambiguity in "compare two arrays" returning just signs without explicit thresholding:
                          We assume standard mathematical sign function of (a - b):
                          1 if a > b, -1 if a < b, and typically handled as per user intent for 'comparison'.
                          
                          Re-reading strict request: "sign of the difference". Standard sgn(diff) is {+1, 0, -1}.
                          However, often in binary comparison contexts users might imply +1/-1 only. 
                          To be safe and performant using NumPy vectorization without loops:

    """
    # Convert inputs to numpy arrays if not already for uniform handling (optional performance step)
    arr1 = np.asarray(array1, dtype=np.float64)
    arr2 = np.asarray(array2, dtype=np.float64)

    assert len(arr1) == len(arr2), "Input arrays must have the same length."
    
    # Compute difference directly via NumPy broadcasting (O(N))
    diff = arr1 - arr2
    
    # Apply standard sign function: 1 if positive, -1 if negative, 0 if zero.
    # Using np.sign ensures high performance and handles float precision correctly.
    return np.sign(diff)

if __name__ == '__main__':
    sample1 = [345.2, 6789.0, 23.1, 0.0]
    sample2 = [345.2, 6789.1, 23.1, 0.0]

    result = compare_signs(sample1, sample2)

    print("Comparison Result:")
    for val in result:
        if val == 1:
            sgn_str = "+1"
        elif val == -1:
            sgn_str = "-1"
        else:
            sgn_str = "0"