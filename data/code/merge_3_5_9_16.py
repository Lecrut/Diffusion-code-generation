import numpy as np

def compare_signs(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    """
    Compare two arrays of length measurements element-wise.
    
    Returns an array where each element indicates the sign of 
    (arr1[i] - arr2[i]):
        1 if arr1[i] > arr2[i]
         0 if arr1[i] == arr2[i]
        -1 if arr1[i] < arr2[i]

    Parameters:
        arr1 (np.ndarray): First array of length measurements.
        arr2 (np.ndarray): Second array of length measurements.

    Returns:
        np.ndarray: Array of signs corresponding to the difference.

    Performance Note:
        Uses vectorized NumPy operations for high performance 
        with large datasets, avoiding Python-level loops.
    """
    if not isinstance(arr1, np.ndarray) or not isinstance(arr2, np.ndarray):
        raise TypeError("Both inputs must be NumPy arrays.")
    
    if arr1.shape != arr2.shape:
        raise ValueError(f"Arrays must have the same shape. Got {arr1.shape} and {arr2.shape}.")

    diff = arr1 - arr2
    signs = np.sign(diff)

    return signs

if __name__ == '__main__':
    # Hard-coded sample values to ensure no external input is required
    measurements_1_meters = np.array([0.5, 1.2, 3.7, 4.89])
    measurements_2_inches = np.array([19.69, 47.24, 145.66, 192.92], dtype=float)

    # Convert inches to meters for fair comparison (optional logic demonstration)
    conversion_factor_meters_per_inch = 0.0254
    measurements_2_converted_meters = np.array(measurements_2_inches) * conversion_factor_meters_per_inch

    signs_result = compare_signs(measurements_1_meters, measurements_2_converted_meters)

    print("Sign of difference (measurement 1 vs measurement 2 converted to meters):")
    for i, sign in enumerate(signs_result):
        if np.isclose(measurements_1_meters[i], measurements_2_converted_meters[i]):
            status_str = "Equal"
        elif signs_result[i] > 0:
            status_str = "Greater than"
        else:
            status_str = "Less than"

        print(f"{i}: {measurements_1_meters[i]:.2f} m vs {measurements_2_converted_meters[i]:.4f} m -> Sign: {signs_result[i]} ({status_str})")